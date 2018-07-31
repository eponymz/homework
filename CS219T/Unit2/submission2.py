class Vehicle:
    def __init__(self):
        self.color = None
        self.hp = None
        self.engine = None
        self.price = None

    def setVehicle(self):
        self.color = raw_input("Color of vehicle: ")
        self.hp = raw_input("Horse Power of vehicle: ")
        self.engine = raw_input("Engine Type of vehicle: ")
        self.price = raw_input("Price of vehicle: ")


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.doors = None
        self.convertible = None

    def setCar(self):
        self.doors = raw_input("Number of doors on car: ")
        self.convertible = raw_input("Is it convertible? ")


class Truck(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.doors = None
        self.wheels = None
        self.flatbed = None

    def setTruck(self):
        self.doors = raw_input("Number of doors on truck: ")
        self.wheels = raw_input("Number of wheels on truck: ")
        self.flatbed = raw_input("Does the truck have a flatbed? ")


class Boat(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.top = None
        self.length = None

    def setBoat(self):
        self.top = raw_input("Does the boat have a top? ")
        self.length = raw_input("Boat length: ")


vehicles = list()


def selectVehicle():
    vehicleType = raw_input("What type of vehicle are you adding? ")
    if vehicleType == 'car':
        car = Car()
        car.setVehicle()
        car.setCar()
        addAnother()
    elif vehicleType == 'truck':
        truck = Truck()
        truck.setVehicle()
        truck.setTruck()
        addAnother()
    elif vehicleType == 'boat':
        boat = Boat()
        boat.setVehicle()
        boat.setBoat()
        addAnother()
    else:
        invalid = raw_input("We only have trucks, boats, and cars. Retry? y/n ")
        if invalid == 'y':
            selectVehicle()
        elif invalid == 'n':
            selectVehicle()
        else:
            print ('Invalid option entered.. Please restart program..')
            return


def addAnother():
    another = raw_input("Would you like to add another vehicle? y/n ")
    if another == 'y':
        selectVehicle()
    elif another == 'n':
        for i in range(len(vehicles)):
            print vehicles
        return
    else:
        addAnother()


selectVehicle()
