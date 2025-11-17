
class Vehicle:
    def __init__(self, vc, vm, vy, ot, vin):
        self.company = vc
        self.model = vm
        self.year = vy
        self.owner_type = ot
        self.vin = vin

    def display(self):
        print("Vehicle Make:", self.company,
              "\n Vehicle Model:", self.model,
              "\n Vehicle Year:", self.year,
              "\n Owner Type:", self.owner_type,
              "\n VIN:", self.vin)

class Car(Vehicle):
    def __init__(self):

class Truck(Vehicle):
    def __init__(self):