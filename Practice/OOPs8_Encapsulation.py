"""name
private __marks
set_marks()
get_marks()
display()
marks validation 0–100
"""

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=0
        self.set_marks(marks)
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")    
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.__marks)
S1=Student("Prak",100)  
S1.set_marks(95)      
S1.display()
mark=S1.get_marks()
print(mark)