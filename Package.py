# class for packages

class Package:
    # Initialize package object
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, truck_id, loading_time,
                 delivery_time, status):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.truck_id = truck_id
        self.loading_time = loading_time
        self.delivery_time = delivery_time
        self.status = status

    # for printing
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.id, self.address, self.city, self.state, self.zip_code,
                                                     self.deadline, self.weight, self.truck_id, self.loading_time,
                                                     self.delivery_time, self.status)

    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.id, self.address, self.city, self.state, self.zip_code,
                                                     self.deadline, self.weight, self.truck_id, self.loading_time,
                                                     self.delivery_time, self.status)

# TO DO
# Update status function
# def update_status(self):
#    self.status = self
