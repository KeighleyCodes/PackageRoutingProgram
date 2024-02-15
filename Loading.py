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


# -- TRUCK DELIVERY -- #

# This is a nearest-neighbor algorithm. ## -- ADD MORE INFO HERE! -------------------
# Space complexity 0(1)
# Time complexity O(n^2), where n is the number of packages
def package_delivery(truck_packages, start_time):
    # Current truck location initialization
    current_truck_location = 0  # Index of hub

    # Initialize current total distance
    total_distance = 0

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
            if current_truck_location < address_index:
                distance = distance_lists[address_index][current_truck_location]

            # Convert distance to float
            distance = float(distance)

            # If current distance is less than the minimum distance, replace minimum distance with current distance
            if distance < min_distance:
                min_distance = distance
                min_package = package

        # If
        if min_package:
            # Set status of package to en route
            min_package.status = 'En Route'

            # Define average truck speed
            truck_speed = 18

            # Calculate trip duration
            trip_duration = distance / truck_speed

            # Add minutes to running time
            running_time += timedelta(minutes=trip_duration)

            # Add distance to total distance
            total_distance += min_distance

            # Timestamp package with delivery time
            min_package.delivery_time = running_time

            # Sets current truck location to address of package
            current_truck_location = address_dictionary.get(min_package.address)

            # Remove package from truck
            truck_packages.remove(min_package.id)

            # Set status of package to delivered
            min_package.status = 'Delivered'

    return total_distance, running_time


# -- TOTAL DISTANCE CALCULATIONS -- #

# Calculates total distance traveled by truck 1
total_distance_truck1, running_time_truck1 = package_delivery(truck1_packages, truck1_loading)

# Rounds total distance to two places after the decimal
truck1_total_distance = round(total_distance_truck1, 2)

# Calculates total distance traveled by truck 2
total_distance_truck2, running_time_truck2 = package_delivery(truck2_packages, truck2_loading)

# Rounds total distance to two places after the decimal
truck2_total_distance = round(total_distance_truck2, 2)

# Calculates total distance traveled by both trucks
total_distance_both = truck1_total_distance + truck2_total_distance


# -- PRINTING PACKAGE STATUS -- #

def print_package_info(package_id, specified_time):
    # Search for package ID
    selected_package = package_hash_table.search(package_id)

    # Check if package exists:
    if selected_package:
        print('                                  ')
        print(f"Package ID: {selected_package.id}")

        # Check the status of the package at the specified time
        if selected_package.delivery_time == specified_time:
            print(f"Status at specified time: Delivered")

            # Print delivery time only if status is 'delivered'
            print(f"Delivery Time: {selected_package.delivery_time}")

        else:
            print(f"Status at specified time: {selected_package.status}")

        print('                                  ')

    else:
        print("Package not found.")

