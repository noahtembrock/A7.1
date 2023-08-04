#Name: Noah Tembrock
#Date: July 23, 2023

print("Welcome to Noah's Garage!")

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        Vehicle.__init__(self, make, model)
        self.num_doors = num_doors

    def get_doors(self):
        return self.num_doors

class Pickup(Vehicle):
    def __init__(self, make, model, bed_length):
        Vehicle.__init__(self, make, model)
        self.bed_length = bed_length

    def get_bed_length(self):
        return self.bed_length

garage = []

while True:
    print("1. Add a car")
    print("2. Add a pickup truck")
    print("3. Quit")
    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        num_doors = input("Enter number of doors: ")
        car = Car(make, model, num_doors)
        garage.append(car)
        print("Car has been added to your garage.")
    elif user_input == 2:
        make = input("Enter pickup truck make: ")
        model = input("Enter pickup truck model: ")
        bed_length = input("Enter bed length: ")
        pickup = Pickup(make, model, bed_length)
        garage.append(pickup)
        print("Truck has been added to your garage.")
    else:
        break

for vehicle in garage:
    print("Make:", vehicle.get_make())
    print("Model:", vehicle.get_model())
    if isinstance(vehicle, Car):
        print("Number of doors:", vehicle.get_doors())
    elif isinstance(vehicle, Pickup):
        print("Bed length:", vehicle.get_bed_length())
    print("\n")
print("Thank you for coming to Noah's Garage.")