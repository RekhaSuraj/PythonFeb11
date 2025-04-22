# class methods:

# Class method: Used to access or modify the class state.
# In method implementation, if we use only class variables,
# then such type of methods we should declare as a class method.
# The class method has a cls parameter which refers to the class.

# Create Class Method Using @classmethod Decorator
# To make a method as class method, add @classmethod decorator before the method definition, and add cls as the first parameter to the method.
#
# The @classmethod decorator is a built-in function decorator. In Python, we use the @classmethod decorator to declare a method as a class method.
# The @classmethod decorator is an expression that gets evaluated after our function is defined.

# What is a Decorator in Python?
# A decorator in Python is a design pattern that lets you add new behavior to a function or class method without modifying its structure.

class Employee:

    company = "HAL"
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # instance method
    def show(self):
        print(self.name, self.age)


    @classmethod
    def class_var(cls):
        print(cls.company)


# obj_Emp = Employee("Vittal",25)
# obj_Emp.show()

# Class method directly from class, it acts as a constructor
Employee.class_var()



