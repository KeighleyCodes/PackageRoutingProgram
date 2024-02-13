# Create HashTable class
# Citing source: WGU W-1_ChainingHashTable_zyBooks_Key-Value.py
# Overall space and time complexity 0(n)
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # Space and time complexity O(n), where n is the initial capacity of the hash table
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # Space and time complexity O(1)
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # Space and time complexity O(1)
    def search(self, key):

        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    # To print each line of hashtable with package csv file
    # Iterates through buckets and key-value pairs in hashtable and appends the string representation of each
    # package object to the result
    # Space and time complexity O(n), where n is the total number of key-value pairs in the hash table
    def __str__(self):
        result = ""
        for bucket_list in self.table:
            for key_value in bucket_list:
                result += str(key_value[1]) + "\n"
        return result
