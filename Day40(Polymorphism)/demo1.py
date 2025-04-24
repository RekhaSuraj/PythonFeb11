# Polymorphism
# Polymorphism in Python is the ability of an object to take many forms.
# In simple words, polymorphism allows us to perform the same action in many different ways.
#
# For example, Jessa acts as an employee when she is at the office. However, when she is at home,
# she acts like a wife. Also, she represents herself differently in different places.
#  Therefore, the same person takes different forms as per the situation.
#
# In polymorphism, a method can process objects differently depending on the class type or data type.


# Examples :
# print(),type(),max(),min(),len(),eval(),count()

# + operator
# It can add more than two number, adding two or more strings

# * Asterisk  : Product of two numbers, repeatition of strings

# Polymorphism With Inheritance
# Polymorphism is mainly used with inheritance. In inheritance, child class inherits the attributes and methods of a parent class.
# The existing class is called a base class or parent class, and the new class is called a subclass or child class or derived class.

# Using method overriding polymorphism allows us to defines methods in the child class that have the same name as the methods in the parent class.
# This process of re-implementing the inherited method in the child class is known as Method Overriding.


class New:

    def new(self):
        print('hello world')


    def new(self):
        print('Welcome')


obj_new = New()
obj_new.new()
# Welcome
#method overriding of new() - which calls only the latest function

