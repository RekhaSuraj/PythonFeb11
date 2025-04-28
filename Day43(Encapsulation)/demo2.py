# Encapsulation:

# Encapsulation : Wrapping data and methods work on data within single unit.


# There are 3 Access Specifiers(Modifiers) :
# 1.Public Access Specifier
# 2.Protected Access Specifier
# 3.Private Access Specifier


# 1.Public Access Specifier : Access from anywhere, Inside class, child class, Outside of class


class Student:

    def __init__(self,Name, Age):
        self.name = Name  #self.name - public attribute (variable)
        self.age = Age   # self.age - public attribute(variable)


    # public method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)


obj_Student = Student("Vittal",25)
obj_Student.display()
# Name: Vittal
# Age: 25

# We can access public attribute and update(modify) them
obj_Student.name = "TestABC"
obj_Student.display()
# Name: TestABC
# Age: 25

