# note: https://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python/2681286

# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):  # set attribute to None
        self.num_wheels = num_wheels


    # def __init__(self, num_wheels=None):  # set attribute to None
    #     if num_wheels is None:
    #         num_wheels = 4

    #   self.num_wheels = num_wheels

    def drive(self):
        return ("vroooom")


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        # auto sets the number of wheels to 2
        super().__init__(num_wheels)

    def drive(self): #method overriding
        super().drive()
        return("BRAAAP!!")


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    print(vehicle.drive())
