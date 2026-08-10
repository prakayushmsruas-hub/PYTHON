"""Create a class:

Book

Attributes:

title
author
price

Create a __str__() method that returns:

Title: Python Basics | Author: Prakayush | Price: 499"""

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Price: {self.price}"


book=Book("Python Basics","Prakayush",499)
print(book)        
        