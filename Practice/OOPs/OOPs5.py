"""Now we're going to make methods return values, which is extremely important in real programs.

Create a class:
Rectangle

It should have:
length
width

Methods:
area()
perimeter()

But here's the rule:
Don't print inside area() or perimeter().
They should return the answer."""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width
    
    def answer(self):
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())

R1=Rectangle(25.5,35.9)
R2=Rectangle(2,3)
R3=Rectangle(25,35)

R1.answer()
R2.answer()
R3.answer()