"""Create a class called:

Employee

Every employee should have:

name
salary

But there should also be a variable:

company = "Google"

Important: company should be common to every employee.

Create 3 employees and display:

Name: ...
Salary: ...
Company: Google"""

class Employee():
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Company name:",Employee.company)  

emp1=Employee("Prak",100000)          
emp2=Employee("Prakayush",150000)          
emp3=Employee("Prakayush Kumar",250000) 
print("-"*10)         
emp1.display()
print("-"*10)
emp2.display()
print("-"*10)
emp3.display()
print("-"*10)