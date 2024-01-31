# load package data into hash table
import csv

from Package import Package
from HashTable import HashTable

# Instantiate hash table
package_hash_table = HashTable()

# Opens CSV Package file and inserts it into hashtable
with open(r"CSV_Files/PackageFile.csv") as packageFile:
    reader = csv.reader(packageFile, delimiter=',')

    # Iterates over each row in Package File
    for row in reader:
        p_id = int(row[0])
        p_address = row[1]
        p_city = row[2]
        p_state = row[3]
        p_zip = row[4]
        p_deadline = row[5]
        p_weight = row[6]
        p_truck = "0"  # initial truck not set
        p_loading_time = "00:00"  # initial time not set
        p_delivery_time = "00:00"  # initial time not set
        p_status = "Waiting"  # initial status set to waiting

        # Creates package object
        package_object = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_truck, p_loading_time,
                                 p_delivery_time, p_status)

        # inserts it into the hash table
        package_hash_table.insert(p_id, package_object)

# Lists of lists to hold distances
distance_lists = []

# Dictionary to hold addresses
address_dictionary = dict()

# Imports CSV Distance table
# Pops off address and adds it to the address dictionary
# Adds remaining data to distance lists of lists
with open(r"CSV_Files/DistanceTable.csv", newline='') as distanceFile:
    reader = csv.reader(distanceFile)

    # Pop address off each row and add to address dictionary. Add remaining row to distance list.
    for index, row in enumerate(reader):
        # Remove address from DistanceTable
        address = row.pop(0)  # variable to store popped address

        # Add removed address to address table
        # Assigns index to each address
        address_dictionary[address] = index

        # Adds remaining row to distance_lists
        distance_lists.append(row)

print(address_dictionary['HUB'])
