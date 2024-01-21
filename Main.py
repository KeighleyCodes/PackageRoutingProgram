# Name: Keighley Manke
# Student ID: 001321515
# Class: WGU C950

# import Excel files as csv
import csv
from ImportCSV import HashTable, packageHashTable
import Package
import HashTable

# import hashtable to Main
from HashTable import HashTable

# Import Distance Table.
with open(r"DistanceTable.csv") as distanceTable:
    reader = csv.reader(distanceTable)

# Import Package File
with open(r"PackageFile.csv") as packageFile:
    reader_2 = csv.reader(packageFile)

# Import Address File
    with open(r"AddressFile.csv") as addressFile:
        reader_3 = csv.reader(addressFile)
#       for row in reader_3:
#           print(row)

print(packageHashTable)
