# class for packages
class Package:
    def __init__(self, package_id, weight, address, city, zip_code, loading_time, delivery_time, deadline, status):
        self.id = package_id
        self.weight = weight
        self.address = address
        self.city = city
        self.loading_time = loading_time
        self.delivery_time = delivery_time
        self.zip_code = zip_code
        self.deadline = deadline
        self.status = status

    # for printing
    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.id, self.weight, self.address, self.city, self.loading_time,
                                               self.delivery_time, self.zip_code, self.deadline, self.status)

    # TO DO: ADD UPDATE STAUTS FUNCTION