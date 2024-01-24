# Name: Keighley Manke
# Student ID: 001321515
# Class: WGU C950

# import Excel files as csv
import csv

from ImportCSV import package_object
from Package import Package

# Lists of lists to hold distances
distance_lists = [[]]

# Dictionary to hold addresses
address_dictionary = dict()

# Import Distance Table.
with open(r"CSV_Files/DistanceTable.csv", newline='') as distanceFile:
    reader = csv.reader(distanceFile)

    # Pop address off each row and add to address dictionary. Add remaining row to distance list.
    for row in reader:
        # Remove address from DistanceTable
        address = row.pop(0)  # variable to store popped address

        # Add removed address to address table
        # Assigns index to each address based on  length of the dictionary.
        address_dictionary[address] = len(address_dictionary)

        # Adds remaining row to distance_lists
        distance_lists.append(row)

# print(distance_lists)


