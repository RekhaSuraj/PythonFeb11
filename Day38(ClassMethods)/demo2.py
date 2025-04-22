# class methods are used for creating factory methods
# Here you're calculating the age from birth_year, and then calling:
# calculate_age is called.
# Inside calculate_age, you compute the age.
# cls(name, age) is the same as:
# Student(name, age) → which calls the __init__ constructor. So your classmethod becomes a kind of alternate constructor!
# The method returns the newly created object.

# In a @classmethod:
# cls refers to the class itself (not an instance).

# @classmethod allows you to create an object without directly calling __init__.


from datetime import date
class Student:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls,name, birth_year):
        # print(date.today().year)
        age = date.today().year - birth_year
        # print(age)
        return cls(name,age)


# obj_stu = Student("Aparna",20)

v1 = Student.calculate_age("Aparna",2000)
print(type(v1))
# <class '__main__.Student'>
print(f'{v1.name} age is {v1.age}')
# Aparna age is 25
