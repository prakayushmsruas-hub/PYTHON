"""Create a parent class:
Person

Attributes:
name
age

Method:
display()

Then create:
Student(Person)

Student should additionally have:
roll_no
branch
And its display() should show all four details."""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)    
class Student(Person):
    def __init__(self,name,age,roll_no,branch):
        super().__init__(name,age) #super() calls the parent constructer
        self.roll_no=roll_no
        self.branch=branch
    def display(self):
        
        print("Roll_no:",self.roll_no)
        print("Branch:",self.branch)
          
S1=Student("Prakayush",18,10,"AIML")    
S1.display()         
S1.display()      
    