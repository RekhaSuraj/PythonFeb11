# Private specifier
# Private members are similar to protected members,
# the difference is that the class members declared private should neither be accessed outside
# the class nor by any base class.
# In Python, there is no existence of Private instance variables that cannot be accessed
# except inside a class.
#
# However, to define a private member prefix the member name with double underscore “__”.

class Student:
    def __init__(self,Name,Marks):
        self.__name = Name #private variable1
        self.__marks = Marks #private variable2

    #private method(instance method)
    def __display(self):
        print(f'Name:{self.__name}\nMarks:{self.__marks}')


    def show(self):
        self.__display()

obj_Student = Student("ABC",90)
obj_Student.show()

# Trying to access private variables directly (will fail)
# obj_Student.__display()
# AttributeError: 'Student' object has no attribute '__display'
# print(obj_Student.__name)
# AttributeError: 'Student' object has no attribute '__name'

# Name mangling
# But... (Name Mangling)
# If you really want to (not recommended), you can access it like this:
# syntax: <object(instance)>._<class_name>__<privateVariable/methodname>
print(obj_Student._Student__name)
print()
obj_Student._Student__display()
# Name:ABC
# Marks:90

