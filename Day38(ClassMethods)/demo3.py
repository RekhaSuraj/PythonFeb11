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

    # instance method
    def show(self):
        print(f'{self.name} age is {self.age}')


# obj_student = Student("Test",30)
# obj_student.show()
# Test age is 30

v1 = Student.calculate_age("Vittal",1996)
v1.show()

# Vittal age is 29

