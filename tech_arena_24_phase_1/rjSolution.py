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

    for row in reader_obj: ### Self explanatory
        r1 = Datacenter(row[0], row[1], row[2], row[3])
        # print(r1) ### You can use this to print out the data centers

###### Reading the different kinds of servers
with open('data/servers.csv') as file_obj: 
    heading = next(file_obj) ### Skips the heading, using next() method 

    reader_obj = csv.reader(file_obj) ### Reads the file

    for row in reader_obj: ### Self explanatory
        r1 = Server(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        print(r1) ### You can use this to print out the data centers


