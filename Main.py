# Name: Keighley Manke
# Student ID:
# WGU C950

import csv
from CreateHashTable import HashTable

# Import Distance Table
with open(r"C:\Users\Owner\OneDrive\Desktop\DistanceTable.csv") as distanceTable:
    reader = csv.reader(distanceTable)

# Import Package File
with open(r"C:\Users\Owner\OneDrive\Desktop\PackageFile.csv") as packageFile:
    reader = csv.reader(packageFile)

# Instantiate hash table
myHash = HashTable()


