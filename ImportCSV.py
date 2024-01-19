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
        pState = package[3]
        pZip = package[4]
        pDeadline = package[4]
        pWeight = package[6]
        pNotes = package[7]
        pTruck = "0"
        pLoadingTime = "00:00"
        pDeliveryTime = "00:00"
        pStatus = "Waiting"  # initial status set to waiting

        # package object
        p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes, pTruck, pLoadingTime,
                    pDeliveryTime, pStatus)

        # print(p)

        # insert it into the hash table
        packageHashTable.insert(pID, p)

        print(packageHashTable)
