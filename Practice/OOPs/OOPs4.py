"""Create a class called Product.
Each product should have:
name
price
quantity
Create these methods:

display()
add_stock()
sell()

What they should do
display()

Print the product's current details.

add_stock()

Ask the user how many items to add and increase quantity.

sell()

Ask how many items the customer wants to buy.
If enough stock exists → decrease quantity
Otherwise → print "Insufficient Stock"""

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
        print("Name:",self.name)    
        print("Price:",self.price)    
        print("Quantity:",self.quantity)    
    def add_stock(self):
        add_quantity=int(input("Enter how many quantity you want to add:"))
        self.quantity+=add_quantity
    def sell(self):
        sell_quantity = int(input("Enter how many quantity you want to sell:"))

        if sell_quantity <= self.quantity:
            self.quantity -= sell_quantity
            print("Sale successful!")
        else:
            print("Insufficient Stock!")
P1=Product("Invesco",50,75) 
P1.display()
P1.add_stock()
P1.sell()    
P1.display()