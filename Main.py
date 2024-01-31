# Name: Keighley Manke
# Student ID: 001321515
# Class: WGU C950

from datetime import datetime, timedelta

from ImportCSV import package_object, distance_lists, address_dictionary
from Package import Package

# Creates lists for each truck, manually loads packages
# TO DO: MANUALLY LOAD PACKAGES ONTO TRUCKS
truck1_packages = []
truck2_packages = []
truck3_packages = []

# Creates arbitrary datetime for future scalability
date_time = datetime(2024, 1, 30)

# Initiates loading time of 08:00 hours
truck1_loading_time = date_time.replace(hour=8, minute=0, second=0)
truck2_loading_time = date_time.replace(hour=8, minute=0, second=0)
truck3_loading_time = date_time.replace(hour=8, minute=0, second=0)

# Assign loading times to packages in each truck's list (assuming it takes 0 minutes to load packages)
for package in truck1_packages:
    package.loading_time = truck1_loading_time

for package in truck2_packages:
    package.loading_time = truck2_loading_time

for package in truck3_packages:
    package.loading_time = truck3_loading_time


# Calculates distance between two points in the list of lists containing distances
def calculate_distance(location1, location2):
    try:
        distance = distance_lists[location1][location2]
        return float(distance)
    # Returns None if there is an out-of-bounds index error
    except IndexError:
        return None


# Starts truck route at hub
# route_truck1 = address_dictionary[["HUB"]]
# route_truck2 = address_dictionary[["HUB"]]
# route_truck3 = address_dictionary[["HUB"]]

# Nearest neighbor algorithm
def delivery_route(current_location, unvisited_location):
    current_location = address_dictionary["HUB"]  # Starts the current location at the hub
    min_distance = float('inf')  # Sets minimum distance to infinity
    nearest_location = None  # initializes empty nearest distance variable

    # Loops over unvisited locations
    for location in unvisited_location:
        distance = calculate_distance(current_location, location)

        if distance < min_distance:
            min_distance = distance
            nearest_location = location

    return nearest_location
