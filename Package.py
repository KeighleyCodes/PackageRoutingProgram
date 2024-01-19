# class for packages

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, truck, loading_time,
                 delivery_time, status):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = truck
        self.loading_time = loading_time
        self.delivery_time = delivery_time
        self.status = status

    # for printing
    def __str__(self):
        return (f'STR is <{self.id} {self.address} {self.city} {self.state} {self.zip_code} {self.deadline}'
                f' {self.weight} {self.notes} {self.truck} {self.loading_time} {self.delivery_time} {self.status}>')

    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.id, self.address, self.city, self.state,
                                                        self.zip_code, self.deadline, self.weight, self.notes,
                                                        self.truck, self.loading_time, self.delivery_time,
                                                        self.status)

    @property
    def human_readable(self):
        return (f'Readable representation is <{self.id} {self.address} {self.city} {self.state} {self.zip_code} '
                f'{self.deadline} {self.weight} {self.notes} {self.truck} {self.loading_time} {self.delivery_time} '
                f'{self.status}>')

# TO DO: ADD UPDATE STATUS FUNCTION
# def update_status(self):
#   self.status = self
