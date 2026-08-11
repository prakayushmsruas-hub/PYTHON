"""Create three classes:
Car
Bike
Bus

Each should have the same method:
move()

But each should print something different:
Car → Car is driving
Bike → Bike is riding
Bus → Bus is moving

Then create a list containing objects of all three classes and use one for loop to call move().

This is your first actual polymorphism program."""

class Car:
    def move(self):
        print("Car is been driven")


class Bike:
    def move(self):
        print("Bike is riding")


class Bus:
    def move(self):
        print("Bus is moving")

Vehicles=[Car(),Bike(),Bus()]
for travel in Vehicles:
    travel.move()        

