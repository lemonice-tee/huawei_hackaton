import numpy as np
import pandas as pd
from seeds import known_seeds
from utils import save_solution
from evaluation import get_actual_demand
import os

def get_my_solution(demand, datacenters, servers, selling_prices):
    solution = []
    # Preprocess data
    # Initialize variables like slots, costs, etc.
    
    # For each time step, determine actions
    for time_step in range(1, 169):
        for dc in datacenters:
            # Predict demand
            predicted_demand = predict_demand(demand, time_step, dc)

            # Make decisions based on predicted demand and server status
            action = determine_action(dc, servers, predicted_demand)

            solution.append({
                "time_step": time_step,
                "datacenter_id": dc['Data-center ID'],
                "server_generation": action['server_generation'],
                "server_id": action['server_id'],
                "action": action['action']
            })
    return solution

def predict_demand(demand, time_step, datacenter):
    """
    Predicts future demand using an exponential moving average (EMA).
    EMA gives more weight to recent demand data to make predictions more responsive to changes.
    This function dynamically updates the demand prediction at each time step.
    """
    alpha = 0.3  # Smoothing factor for EMA
    dc_id = datacenter['Data-center ID']
    
    # Filter the demand data for the specific datacenter and up to the current time step
    demand_history = demand[(demand['datacenter_id'] == dc_id) & (demand['time_step'] <= time_step)].copy()
    
    # Calculate EMA on demand history
    demand_history['ema'] = demand_history['demand'].ewm(alpha=alpha, adjust=False).mean()
    
    # Predict demand for the next time step by assuming the latest EMA as the predicted demand
    if not demand_history.empty:
        predicted_demand = demand_history.iloc[-1]['ema']
    else:
        predicted_demand = 0  # Default to 0 if there is no history
    
    return predicted_demand

import uuid

def assign_unique_server_ids(servers):
    """
    Assigns a unique ID to each server in the servers list.
    """
    unique_servers = []
    for index, server in servers.iterrows():
        server_id = f"{server['Data-center ID']}-{server['Server Type']}-{uuid.uuid4()}"
        server['Server ID'] = server_id
        unique_servers.append(server)
    
    return pd.DataFrame(unique_servers)

def determine_action(datacenter, servers, predicted_demand):
    """
    Determine the optimal action (buy, move, hold, dismiss) for servers in a datacenter.
    The function evaluates server utilization, capacity, lifespan, and profit to make decisions.
    """
    actions = []
    dc_id = datacenter['Data-center ID']
    capacity = datacenter['Slots Capacity']
    energy_cost = datacenter['CostofEnergy']
    available_slots = capacity - sum(server['Slots Size'] for server in servers if server['datacenter_id'] == dc_id)
    
    for _, server in servers.iterrows():
        server_id = server['Server ID']
        server_type = server['Server Type']
        server_lifespan_ratio = server['Operating Time'] / server['Life Expectancy']
        server_utilization = predicted_demand / server['Capacity']
        server_profit = server_utilization * server['Selling Price'] - server['Energy Consumption'] * energy_cost
        
        if available_slots > 0 and predicted_demand > server['Capacity']:
            actions.append({"datacenter_id": dc_id, "server_id": server_id, "action": "buy"})
            available_slots -= server['Slots Size']
        
        elif server_utilization < 0.5 and predicted_demand > server['Capacity']:
            actions.append({"datacenter_id": dc_id, "server_id": server_id, "action": "move"})
        
        elif server_lifespan_ratio < 1.0 and server_profit > 0:
            actions.append({"datacenter_id": dc_id, "server_id": server_id, "action": "hold"})
        
        else:
            actions.append({"datacenter_id": dc_id, "server_id": server_id, "action": "dismiss"})
    
    return actions


# Main loop
seeds = known_seeds('training')
demand = pd.read_csv('./data/demand.csv')
datacenters = pd.read_csv('./data/datacenters.csv')
servers = pd.read_csv('./data/servers.csv')
selling_prices = pd.read_csv('./data/selling_prices.csv')

# Assign unique IDs to servers
servers = assign_unique_server_ids(servers)

for seed in seeds:
    np.random.seed(seed)
    actual_demand = get_actual_demand(demand)
    solution = get_my_solution(actual_demand, datacenters, servers, selling_prices)
    save_solution(solution, f'./output/{seed}.json')