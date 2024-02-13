# load package data into hash table
import csv

from Package import Package
from HashTable import HashTable
from datetime import datetime, timedelta

# Overall space and time complexity is O(n^2) due to the nested loops for
# both the address and distance processing and the truck delivery algorithm.

# -- PACKAGES -- #

# Instantiate hash table for packages
package_hash_table = HashTable()

# Opens CSV Package file and inserts it into hashtable
# Space and time complexity O(n), where n is the number of packages
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
# Space and time complexity O(n^2), where n is the number of addresses
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

# Creates a list for each truck, manually loads packages
# Space and time complexity O(1)
truck1_packages = [1, 2, 4, 6, 7, 12, 13, 17, 22, 24, 25, 26, 27, 29, 31, 32, 33, 35, 39, 40]
truck2_packages = [3, 5, 8, 9, 10, 11, 14, 15, 16, 18, 19, 20, 21, 23, 28, 30, 34, 36, 37, 38]

# Sets truck loading times
truck1_loading = datetime(2024, 1, 31, 8, 0)
truck2_loading = datetime(2024, 1, 31, 9, 5)

# Timestamp each package with loading time
truck1_timestamp = datetime(2024, 1, 31, 8, 0)
truck2_timestamp = datetime(2024, 1, 31, 9, 15)


# -- TRUCK DELIVERY -- #

# -- TO DO -- #
# Update status function
# def update_status(status):
#    package_status = status

# Space complexity 0(1)
# Time complexity O(n^2), where n is the number of packages
def package_delivery(truck_packages, start_time):
    # Current truck location initialization
    current_truck_location = 0  # Index of hub

    # Minimum distance initialization
    min_distance = float('inf')  # Positive infinity to ensure any distance will be less

    # Minimum packages initialization
    min_package = None

    # Current running time
    running_time = start_time

    # Initialize distance with a default value
    distance = 0

    while truck_packages:

        # Reset min_distance for each iteration
        min_distance = float('inf')

        # Fetch package object from hash table
        for package_id in truck_packages:
            package = package_hash_table.search(package_id)

            # Use address field to retrieve corresponding index
            address_index = address_dictionary.get(package.address)

            # Retrieve distances from distance lists
            distance = distance_lists[current_truck_location][address_index]

            # Convert distance to float
            distance = float(distance)

            # If current distance is less than the minimum distance, replace minimum distance with current distance
            if distance < min_distance:
                min_distance = distance
                min_package = package

        if min_package:
            # Define truck speed
            truck_speed = 18  # Assuming truck speed is constant

            # Calculate trip duration
            trip_duration = distance / truck_speed

            # Add minutes to running time
            running_time += trip_duration

            # Timestamp package with delivery time
            min_package.delivery_time = running_time

            # Remove package from truck
            truck_packages.remove(min_package.id)

            # Set status of package to delivered
            min_package.status = 'Delivered'

    # Check if all packages were successfully delivered
    all_delivered = len(truck_packages) == 0

    return all_delivered


package_delivery(truck1_packages, truck1_loading)
package_delivery(truck2_packages, truck2_loading)
