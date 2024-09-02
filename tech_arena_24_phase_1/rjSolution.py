#!/usr/bin/env python3

### Custom Imports
from customClasses.datacenter import *
from customClasses.servers import *

### Other Imports
import pandas as pd
import csv 

##### IMPORTS ABOVE

"""
    ========================================================================================
    |   NOTE ----------------                                                              |
    |   I was just using the CSV module because it's better for reading smaller files      |
    |   For the larger datasets, it might be best to use panda                             |
    |                                                                                      |
    |   - RJ                                                                               |
    ========================================================================================
"""

##### Reading the data centers

with open('data/datacenters.csv') as file_obj: 
    heading = next(file_obj) ### Skips the heading, using next() method 

    reader_obj = csv.reader(file_obj) ### Reads the file

    ### Header
    print(f"{'Datacenter':<15} {'Cost Energy':>12} {'Latency':>10} {'Slots':>10} {'Cost':>10} {'Spent':>10}")

    for row in reader_obj: ### Self explanatory
        r1 = Datacenter(row[0], row[1], row[2], row[3])

        # print(r1) ### You can use this to print out the data centers

print() ### Just to create a gap

###### Reading the different kinds of servers
with open('data/servers.csv') as file_obj: 
    heading = next(file_obj) ### Skips the heading, using next() method 

    reader_obj = csv.reader(file_obj) ### Reads the file

    ### Header
    print(f"{'Server Generation':<20} {'Type':6} {'Purchase Price':>15} {'Slot Size':>10} {'EnergyCon':>10} {'Capacity':>10} {'Life Exp.':>10}  {'Cost to Move.':>15}  {'Maintenance.':>15}")

    for row in reader_obj: ### Self explanatory
        r1 = Server(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

        # print(r1) ### You can use this to print out the servers

##################### Above is all setup based code
##################### Below will be the main production

csv_file_path = 'your_file.csv'
chunk_size = 1  ### Reading 1 row at a time

chunk_iterator = pd.read_csv("data/demand.csv", chunksize=chunk_size)

i = 0 ### Counter just to read the first 5 lines

for chunk in chunk_iterator:
    
    if i == 5: ### Counter just to read the first 5 lines
        break

    row = chunk.iloc[0]
    print(row.to_dict())

    i = i + 1