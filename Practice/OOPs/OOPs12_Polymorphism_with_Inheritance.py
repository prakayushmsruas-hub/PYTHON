class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bhow Bhow!")

class Cat(Animal):
    def sound(self):
        print("Meow Meow!") 

class Cow(Animal):
    def sound(self):
        print("Meh Meh!")              

dog=Dog()
cat=Cat()
cow=Cow()

Animals=[dog,cat,cow]
for animal in Animals:
    animal.sound()