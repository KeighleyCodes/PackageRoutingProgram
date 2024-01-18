# class for packages
import csv


class Package:
    def __init__(self, package_id, address, city, zip_code, deadline, weight, truck, loading_time, delivery_time,
                 status):
        self.id = package_id
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.truck = truck
        self.loading_time = loading_time
        self.delivery_time = delivery_time
        self.status = status

    # for printing
    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s" % (
            self.id, self.weight, self.address, self.city, self.zip_code, self.loading_time,
            self.deadline, self.weight, self.truck, self.loading_time, self.delivery_time,
            self.status)

    # TO DO: ADD UPDATE STATUS FUNCTION
    def update_status(self):
        self.status = self
