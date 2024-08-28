
import numpy as np
import pandas as pd
from seeds import known_seeds
from utils import save_solution
from evaluation import get_actual_demand


def get_my_solution(d):
    # This is just a placeholder.
    '''
    MY PLAN // CODE 
    - make a "queue" of all servers
    - check dc demand
    - check that server(s) will not exceed 90% usage by next timestamp
        - if yes: dismiss
        - if  no: check to see if there is a server that better meets dc server demand
            - if yes: move current server and replace w server in queue
            - if  no: hold
        - if server life expectancy exceeded and no other server: buy
    '''
    
    return [{}]


seeds = known_seeds('training')

demand = pd.read_csv('./data/demand.csv')
for seed in seeds:
    # SET THE RANDOM SEED
    np.random.seed(seed)

    # GET THE DEMAND
    actual_demand = get_actual_demand(demand)

    # CALL YOUR APPROACH HERE
    solution = get_my_solution(actual_demand)

    # SAVE YOUR SOLUTION
    save_solution(solution, f'./output/{seed}.json')

