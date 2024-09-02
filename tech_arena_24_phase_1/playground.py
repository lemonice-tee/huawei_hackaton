import csv 
  
# Open file 
with open('data/datacenters.csv') as file_obj: 
      
    # Skips the heading, using next() method 
    heading = next(file_obj) 
    reader_obj = csv.reader(file_obj) ### Reads the file

    for row in reader_obj: ### Self explanatory
        print(row) 