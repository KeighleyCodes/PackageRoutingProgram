# load package data into hash table
import csv

from Package import Package
from HashTable import HashTable
from datetime import datetime, timedelta

# -- PACKAGES -- #

# Instantiate hash table for packages
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
        p_truck = None  # initial truck not set
        p_loading_time = None  # initial loading time not set
        p_delivery_time = None  # initial time not set
        p_status = "Waiting"  # initial status set to waiting

        # Creates package object
        package_object = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_truck, p_loading_time,
                                 p_delivery_time, p_status)

        # Inserts package object into hash table
        package_hash_table.insert(p_id, package_object)


# -- ADDRESSES AND DISTANCES -- #

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


# -- TRUCK LOADING -- #

# Creates a dictionary of lists for each truck, manually loads packages
# Dictionary used for easier iteration
truck_packages = {
    'truck1': [1, 2, 4, 6, 7, 12, 13, 17, 22, 24, 25, 26, 27, 29, 31, 32, 33, 35, 39, 40],
    'truck2': [3, 5, 8, 9, 10, 11, 14, 15, 16, 18, 19, 20, 21, 23, 28, 30, 34, 36, 37, 38]
}

# Sets truck loading times
loading_time = {
    'truck1': (datetime(2024, 1, 31, 8, 0)),
    'truck2': (datetime(2024, 1,31,9,5))
}

# Timestamp each package with loading time
current_time = {
    'truck1': (datetime(2024, 1, 31, 8, 0)),
    'truck2': (datetime(2024, 1,31,9,15))
}


# -- TRUCK DELIVERY -- #

def package_delivery(package_list, start_time):

    # Current truck location initialization
    current_truck_location = 0  # Index of hub

    # Minimum distance initialization
    min_distance = float('inf')  # Positive infinity to ensure any distance will be less

    # Minimum packages initialization
    min_packages = None

    # While trucks are not empty
    while any(truck_packages.values()):
        for package_ids in package_list:
            # Fetch package object from hash table
            package = package_hash_table.search(package_ids)
            print(package)

            # Use address field to retrieve corresponding index
            address_index = address_dictionary[package.address]

            # Retrieve distances from distance lists
            distance = distance_lists[current_truck_location][address_index]

            # If current distance is less than the minimum distance, replace minimum distance with current distance
            if distance < min_distance:
                min_distance = distance

            # Update the truck current location
            current_truck_location = address_index

