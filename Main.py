# Name: Keighley Manke
# Student ID: 001321515
# Class: WGU C950

# import Excel files as csv
import csv
from ImportCSV import package_hash_table

# Import Distance Table
with open(r"DistanceTable.csv") as distanceTable:
    reader = csv.reader(distanceTable)

# Import Package File
# with open(r"PackageFile.csv") as packageFile:
#    reader_2: reader = csv.reader(packageFile)
#    for row in reader_2:
#       print(row)

# Import Address File
with open(r"AddressFile.csv") as addressFile:
    reader_3 = csv.reader(addressFile)

#print(packageHashTable)
