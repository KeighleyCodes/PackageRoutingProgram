# Create HashTable class
# Citing source: WGU W-1_ChainingHashTable_zyBooks_Key-Value.py
class CreateHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
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
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None


if __name__ == '__main__':
    def __init__(self, package_id, weight, address, city, zip_code, loading_time, delivery_time, deadline, truck,
                 status):
        self.id = package_id
        self.weight = weight
        self.address = address
        self.city = city
        self.loading_time = loading_time
        self.delivery_time = delivery_time
        self.zip_code = zip_code
        self.deadline = deadline
        self.truck = truck
        self.status = status


def __repr__(self):
    return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.id, self.weight, self.address, self.city, self.loading_time,
                                              self.delivery_time, self.zip_code, self.deadline, self.truck,
                                              self.status)
