import pandas as pd
#import sys
## CHECK END OF CODE FOR NOTE

# Load the CSV files into DataFrames
servers_df = pd.read_csv('./data/servers.csv')
data_centers_df = pd.read_csv('./data/datacenters.csv')
demand_df = pd.read_csv('./data/demand.csv')

## CHECKING ABOVE WORKS
#sys.stdout.write(f"Servers: {len(servers_df)}\n")

## CREATE THE SERVER ID
used_id = []
for id in range(1, 1000):
    if id not in used_id:
        server_id = id
    else:
        used_id.append(id)


# assigning new id to servers in server.csv
assignment = {}
for index, row in servers_df.iterrows():
    server_generation = row['server_generation']
    assignment[index] = [server_generation]

# Prints assignment data frame
assignment_df = pd.DataFrame.from_dict(assignment, orient='index', columns=['server_generation'])
print(assignment_df)


## NOTE: CURRENTLY THIS CODE WORKS BY ASSIGNING AN ID TO THE SERVER WITHOUT INTERACTING W SERVER CSV, WILL BE CHANGED TO DO SO SUCH THAT THE SERVERS CAN BE ASSIGNED TO THE DATA CENTRE
    
    
'''
    server_id = row['Server ID']
    server_type = row['Server Type']
    server_lifespan_ratio = row['Life Expectancy'] / row['Operating Time']
    server_utilization = demand_df['demand'].mean() / row['Capacity']
    server_profit = server_utilization * row['Selling Price'] - row['Energy Consumption'] * row['Cost of Energy']
    '''
    
'''

# Example assignment logic:
# - Assign servers to data centers based on the order they appear, cycling through data centers.
# - This logic can be modified based on your specific criteria, such as matching location or checking capacity.

# Initialize a list to store server assignments
assignments = []

# Cycle through data centers
data_center_index = 0

for _, server in servers_df.iterrows():
    # Get the current data center
    data_center = data_centers_df.iloc[data_center_index]

    # Assign the server to the data center
    assignments.append({
        'Server ID': server['Server ID'],
        'Data-center ID': data_center['Data-center ID'],
        'Server Type': server['Server Type'],
        'Location': data_center['Location']

        ''
        
    })

    # Move to the next data center, cycling back to the first if needed
    data_center_index = (data_center_index + 1) % len(data_centers_df)

# Create a new DataFrame for the assignments
assignments_df = pd.DataFrame(assignments)

# Save the assignments to a new CSV file
assignments_df.to_csv('server_assignments.csv', index=False)

print(
    "Servers have been assigned to data centers and saved to 'server_assignments.csv'"
)

'''