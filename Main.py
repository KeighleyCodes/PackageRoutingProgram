# Name: Keighley Manke
# Student ID:
# WGU C950

from idlelib.multicall import r
import pandas as pd
import csv
from CreateHashTable import HashTable

# Import Distance Table
with open(r"C:\Users\Owner\OneDrive\Desktop\WGUPS Distance Table.csv") as distanceTable:
    reader = csv.reader(distanceTable)

# Import Package File
with open(r"C:\Users\Owner\OneDrive\Desktop\WGUPS Package File.csv") as packageFile:
    reader = csv.reader(packageFile)

# Instantiate hash table
myHash = HashTable()


