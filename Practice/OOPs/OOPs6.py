"""Now let's level up slightly.

Create:
class Circle:

Attribute:
radius

Methods:
area()
circumference()
is_larger(other)

area() → return area.
circumference() → return circumference.
is_larger(other) → compare the areas of two Circle objects and return True or False."""
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*math.pi*self.radius
    def area(self):
        return math.pi*(self.radius**2) 
    def is_larger(self,other):
        if self.area()>other.area():
            return True
        elif self.area()<other.area():
            return False
        else:
            return "Equal"

C1=Circle(5)
C2=Circle(10)
print(C1.circumference())
print(C2.circumference())

print(C1.area())
print(C2.area())

print(C2.is_larger(C1))    