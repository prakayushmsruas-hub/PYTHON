"""
Create a Student class that:
Takes name
Takes age
Takes marks
Has a display() method
Creates 2 student objects
Displays both students

"""

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("NAME:",self.name,"\n","AGE:",self.age,"\n","MARKS:",self.marks)    
student1=Student("Prak",18,100)   
student2=Student("Div",17,100)     
student1.display()
student2.display()