# Example to remember access specifiers

class Employee:

    def __init__(self, Name, Age, Salary, Gender, Country, Profession):
        self.__name = Name #private variable1
        self.__age = Age #private variable 2
        self.__salary = Salary #private variable 3
        self._gender = Gender #protcted variable 1
        self.country = Country #public variable 1
        self._profession = Profession #protected variable2


obj = Employee("TestName",25,60000,"Male","India","IT")

print(obj.country) #public
print(obj._gender) #protected (not recommended)
print(obj._profession) #protected (not recommended)
# print(obj.__name) # AttributeError: 'Employee' object has no attribute '__name'
# using name mangling
print(obj._Employee__name)
print(obj._Employee__age)
print(obj._Employee__salary)

# India
# Male
# IT
# TestName
# 25
# 60000

