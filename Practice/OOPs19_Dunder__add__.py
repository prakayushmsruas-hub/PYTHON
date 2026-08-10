class Money:
    def __init__(self,amount):
        self.amount=amount
    def __add__(self, other):
        
        return Money(self.amount + other.amount)    
m1=Money(1000)        
m2=Money(1500)        
m3=m1+m2
print(m3.amount)