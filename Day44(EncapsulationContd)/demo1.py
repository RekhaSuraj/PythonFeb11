# Protected members are those members of the class that cannot be accessed
# outside the class but can be accessed from within the class and its subclasses.
# To accomplish this in Python, just follow the convention by prefixing the name of the member by
# a single underscore “_”.
# By convention, it means:
# 🔹 "This is meant for internal use only. Please don't access it outside the class or subclass."
# 🔹 But technically, Python still allows access — it's just a warning to developers.

class Employee:

    def __init__(self,Name,Age,Salary):
        self._name = Name #protected variable1
        self._age = Age #protected variable2
        self._salary = Salary #protected variable3

    #protected method(instance method)
    def _display(self):
        print(f'Name:{self._name}\nAge:{self._age}\nSalary:{self._salary}')


class Manager(Employee):

    def show(self):
        self._display()
        # super()._display()


obj_Manager = Manager("ABC",30,50000)
obj_Manager.show()
print()
#Technically, you can still access protected members from outside (not recommended)
obj_Manager._display()
print(obj_Manager._name)

