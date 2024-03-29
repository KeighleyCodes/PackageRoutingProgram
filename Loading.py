# load package data into hash table
import csv

from Package import Package
from HashTable import HashTable
from datetime import timedelta

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
        p_status = "At hub"  # initial status set to waiting

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
truck1_packages = [1, 14, 15, 24, 26, 29, 30, 31, 34, 37, 38, 39, 40]
truck2_packages = [3, 6, 13, 16, 18, 20, 25, 27, 28, 32, 33, 35, 36]
truck3_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23]

# Assign truck ID to each package
for package_id in truck1_packages:
    # Searches for package in package hash table
    package_object = package_hash_table.search(package_id)
    # If package is found
    if package_object:
        # Assign truck ID
        package_object.truck_id = 1
        # Assign loading time
        package_object.loading_time = timedelta(hours=8, minutes=30)

# Assign truck ID to each package
for package_id in truck2_packages:
    # Searches for package in package hash table
    package_object = package_hash_table.search(package_id)
    # If package is found
    if package_object:
        # Assign truck ID
        package_object.truck_id = 2
        # Assign loading time
        package_object.loading_time = timedelta(hours=9, minutes=5)

# Assign truck ID to each package
for package_id in truck3_packages:
    # Searches for package in package hash table
    package_object = package_hash_table.search(package_id)
    # If package is found
    if package_object:
        # Assign truck ID
        package_object.truck_id = 3
        # Assign loading time
        package_object.loading_time = timedelta(hours=10, minutes=30)

# Sets truck loading times
truck1_loading = timedelta(hours=8, minutes=30)
truck2_loading = timedelta(hours=9, minutes=5)
truck3_loading = timedelta(hours=10, minutes=30)


# -- TRUCK DELIVERY -- #

# This is a nearest-neighbor algorithm. Given a list of packages and their addresses, it iteratively selects the
# package nearest to the current truck location and delivers it. The algorithm calculates distances between the
# current location and package destinations and updates delivery statuses and timestamps for each package,
# keeping track of total distance traveled and the final delivery time.
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

            # Retrieve distances from distance lists and convert to float
            if current_truck_location <= address_index:
                distance = float(distance_lists[address_index][current_truck_location])

            else:
                distance = float(distance_lists[current_truck_location][address_index])

            # If current distance is less than the minimum distance, replace minimum distance with current distance
            if distance < min_distance:
                min_distance = distance
                min_package = package

        # If current distance less than minimum distance, replace minimum distance with current distance
        if min_package:
            # Set status of package to en route
            min_package.status = 'En Route'

            # Define average truck speed
            truck_speed = 18

            # Calculate trip duration in minutes (convert hours to minutes)
            trip_duration = (min_distance / truck_speed) * 60

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

# Call package_delivery function and store return values
total_distance_truck1, running_time_truck1 = package_delivery(truck1_packages, truck1_loading)
total_distance_truck2, running_time_truck2 = package_delivery(truck2_packages, truck2_loading)
total_distance_truck3, running_time_truck3 = package_delivery(truck3_packages, truck3_loading)

# Rounds total distances to two places after the decimal
truck1_total_distance = round(total_distance_truck1, 2)
truck2_total_distance = round(total_distance_truck2, 2)
truck3_total_distance = round(total_distance_truck3, 2)

# Calculates total distance traveled by both trucks
total_distance_all = truck1_total_distance + truck2_total_distance + truck3_total_distance


# -- PRINTING PACKAGE STATUS -- #

# Function to search for each package by package ID at any time specified by the user and display its info
# It has a special case for package 9 to update its address after 10:20
# Space complexity O(1)
# Time complexity O(1) because there will be no collisions in the buckets with the small amount of data & chaining
# hashtable
def individual_package_info(package_id, specified_time, specified_date):
    # Search for package ID
    selected_package = package_hash_table.search(package_id)

    # Check if package exists
    if selected_package:

        # Special case for package ID 9: Address is updated after 10:20
        # Check if the specified time is after 10:20
        if specified_time >= timedelta(hours=10, minutes=20):

            # If package ID is 9 and address has not yet been updated, update address and mark as updated
            if selected_package.id == 9 and not selected_package.address_updated:
                selected_package.address = '410 S. State St.'
                selected_package.address_updated = True
        else:
            # If the specified time is before 10:20, revert to the original address
            if selected_package.id == 9 and selected_package.address_updated:
                selected_package.address = '300 State St.'
                selected_package.address_updated = False

        # Changes status of package depending on where the package is
        if selected_package.delivery_time:

            # Package is set to hub if it hasn't been loaded
            if specified_time < selected_package.loading_time:
                selected_package.status = 'At hub'

            # Package is en route if it is loaded onto truck and not yet delivered
            elif specified_time < selected_package.delivery_time:
                selected_package.status = 'En route'

            # Package is set to delivered when appropriate
            else:
                selected_package.status = 'Delivered'

        # If package not found message is printed
        else:
            selected_package.status = 'Package not found'

        # Prints all package info
        print(f"\nPackage ID: {selected_package.id}")
        print(f"Address: {selected_package.address}")
        print(f"City: {selected_package.city}")
        print(f"Zip Code: {selected_package.zip_code}")
        print(f"Weight: {selected_package.weight}")
        print(f"Deadline: {selected_package.deadline}")
        print(f'Truck ID: {selected_package.truck_id}')
        print(f"Status at {specified_time}: {selected_package.status}")

        # Print delivery time if the package is delivered
        if selected_package.status == 'Delivered':
            print(f"Delivery Time: {selected_package.delivery_time}")

    # If package not found
    else:
        print("Package not found.")


# Function to print all package info. It has a special case for package 9 to update its address after 10:20
# Space complexity O(1)
# Time complexity O(1) because there will be no collisions in the buckets with the small amount of data & chaining
# hashtable
def all_package_info(specified_time, specified_date):
    # Starts with the first package
    package_id = 1
    # Flag to check if any package is found
    package_found = False

    print("All Package Information:")
    while True:
        # Retrieve the package from the hashtable
        selected_package = package_hash_table.search(package_id)

        # Check if package exists
        if selected_package:
            # Set flag to True since package is found
            package_found = True

            # Check if the specified time is after 10:20
            if specified_time >= timedelta(hours=10, minutes=20):
                # Special case for package ID 9: update address after 10:20
                if selected_package.id == 9 and not selected_package.address_updated:
                    selected_package.address = '410 S. State St.'
                    selected_package.address_updated = True
            else:
                # If the specified time is before 10:20 and the address has been updated, revert to the original address
                if selected_package.id == 9 and selected_package.address_updated:
                    selected_package.address = '300 State St.'
                    selected_package.address_updated = False

            # Check the status of the package at the specified time
            if selected_package.delivery_time:
                if specified_time < selected_package.loading_time:
                    selected_package.status = 'At hub'
                elif specified_time < selected_package.delivery_time:
                    selected_package.status = 'En route'
                else:
                    selected_package.status = 'Delivered'

            # Print package information
            print(f"\nPackage ID: {selected_package.id}, Address: {selected_package.address}")
            print(f"City: {selected_package.city}")
            print(f"Zip Code: {selected_package.zip_code}")
            print(f"Weight: {selected_package.weight}")
            print(f"Deadline: {selected_package.deadline}")
            print(f'Truck ID: {selected_package.truck_id}')
            print(f"Status at {specified_time}: {selected_package.status}")

            # Print delivery time if the package is delivered
            if selected_package.status == 'Delivered':
                print(f"Delivery Time: {selected_package.delivery_time}")

        else:
            # If no package is found and the loop has iterated over all package IDs, break the loop
            if package_found:
                break
            else:
                print("Package not found.")

        # Move to the next package ID
        package_id += 1
