"""Create:
Father
 └── work()
Mother
 └── cook()

Child(Father, Mother)

work() should print:
Father is working

cook() should print:
Mother is cooking

Then create a Child object and call both methods."""

class Father:
    def work(self):
        print("Father is working")
class Mother:
    def cook(self):
        print("Mother is cooking")
class Child(Father,Mother) :
    pass

Children=Child()
Children.work()
Children.cook()

