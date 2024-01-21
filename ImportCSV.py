# load package data into hash table
import csv

from Package import Package
from HashTable import HashTable

packageHashTable = HashTable()

with open(r"PackageFile.csv") as packageFile:
    reader = csv.reader(packageFile, delimiter=',')

    for row in reader:
        p_id = int(row[0])
        p_address = row[1]
        p_city = row[2]
        p_state = row[3]
        p_zip = row[4]
        p_deadline = row[5]
        p_weight = row[6]
        p_notes = ""
        p_truck = "0"
        p_loading_time = "00:00"
        p_delivery_time = "00:00"
        p_status = "Waiting"  # initial status set to waiting

        # package object
        package_object = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_notes, p_truck, p_loading_time,
                                 p_delivery_time, p_status)

        # print(package_object)

        # insert it into the hash table
        packageHashTable.insert(p_id, package_object)

# print(packageHashTable)
