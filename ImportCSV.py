# load package data into hash table
import csv

from Package import Package
from HashTable import CreateHashTable

packageHashTable = CreateHashTable()
with open(r"PackageFile.csv") as packageFile:
    reader = csv.reader(packageFile, delimiter=',')
    for package in packageFile:
        pID = int(package[0])
        pAddress = package[1]
        pCity = package[2]
        pZip = package[3]
        pDeadline = package[4]
        pWeight = package[5]
        pTruck = package[6]
        pLoadingTime = package[7]
        pDeliveryTime = package[8]
        pStatus = "Waiting"  # initial status set to waiting

        # package object
        p = Package(pID, pAddress, pCity, pZip, pDeadline, pWeight, pTruck, pLoadingTime, pDeliveryTime, pStatus)
        print(p)

        # insert it into the hash table
        packageHashTable.insert(pID, p)
