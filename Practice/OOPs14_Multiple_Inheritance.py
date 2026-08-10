class Father:
    def __init__(self,father_name,father_skill):
        self.father_name=father_name
        self.father_skill=father_skill
    def display_father(self):
        print("Father:", self.father_name)
        print("Father's Skill:", self.father_skill)    

class Mother:
    def __init__(self,mother_name,mother_skill):
        self.mother_name=mother_name
        self.mother_skill=mother_skill        
    def display_mother(self):
        print("Mother:", self.mother_name)
        print("Mother's Skill:", self.mother_skill)    

class Child(Father,Mother):
    def __init__(self,father_name,father_skill,mother_name,mother_skill,child_name):
        Father.__init__(self,father_name,father_skill) 
        Mother.__init__(self,mother_name,mother_skill)
        self.child_name=child_name
    def display(self):
        print(self.child_name)    
ch=Child("ABC","SDE","DEF","HouseWife","Prakayush")
ch.display()
ch.display_father()
ch.display_mother()
# print(Child.mro())    