"""Parent class
Animal
Method:
eat()

which prints:
Animal is eating
Child classes
Dog
Cat
Both should inherit from Animal.

Then create one Dog and one Cat object and call eat() on both.
Don't use __init__ yet."""

class Animal:
    def eat(self):
        print("Animal is Eating")
class Dog(Animal):
    def bark(self):
        print("bhow bhow!")
class Cat(Animal):
    def meow(self):
        print("meow meow!")
dog=Dog()
cat=Cat()
dog.eat()
cat.eat()
dog.bark()
cat.meow()