"""
Create a class called BankAccount.
It should have:
name
balance

And methods:
deposit()
withdraw()
display_balance()"""

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self):
        depo_amount=float(input("Enter the amount you want to deposit:"))
        self.balance+=depo_amount
        print("You have successfully deposited:",depo_amount)
        print("Now your balance is:",self.balance)
    def withdraw(self):
        withdrawal_amt=float(input("Enter the amount you want to withdraw:"))
        if withdrawal_amt<=self.balance:
            self.balance-=withdrawal_amt
            print("Successfully withdrawed",withdrawal_amt)
        else:
            print("Insufficient Balance!")        
    def display_balance(self):
        print("Current Balance:",self.balance)  


Bankacc1=BankAccount("Prakayush",10000)        
Bankacc2=BankAccount("Prak",10000)        
Bankacc1.display_balance()
Bankacc2.display_balance()

Bankacc1.deposit()

Bankacc1.display_balance()
Bankacc2.display_balance()

Bankacc2.withdraw()

Bankacc1.display_balance()
Bankacc2.display_balance()
# def menu():
#         print("-"*10,"MENU","-"*10)   
#         print("1.Deposit") 
#         print("2.Withdraw")
#         print("3.Display Balance")
#         print("4.Exit") 
# Bankacc1=BankAccount("Prakayush",5000)      
# while True:
#     menu()
#     choice=int(input("Enter (1/2/3/4):"))
#     if choice==1:
#         Bankacc1.deposit()
#     elif choice==2:
#         Bankacc1.withdraw()
#     elif choice==3:
#         Bankacc1.display_balance()
#     elif choice==4:
#         break
#     else:
#         print("Invalid Choice!")                  

