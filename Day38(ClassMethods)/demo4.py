# static methods:
# A @staticmethod is a method inside a class that:

# Does not need access to self (object).

# Does not need access to cls (class).

# It behaves like a normal function, but is put inside a class for organization.
# When to use @staticmethod:
# When the method doesn’t depend on class or object data.
# When you want to group utility functions logically inside a class.


class Arithmetic_Tool:

    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def multiply(x,y):
        return x*y

var1 = Arithmetic_Tool.add(5,6)
print(var1)
# 11

var2 = Arithmetic_Tool.multiply(20,30)
print(var2)
# 600


