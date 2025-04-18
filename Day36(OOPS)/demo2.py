class Person:

    def __init__(self,Name, Age, Salary):
        self.p_name = Name # instance variable 1
        self.p_Age = Age # instance variable 2
        self.p_Salary = Salary #instance variable 3

        print(self.p_name)
        print(self.p_Age)
        print(self.p_Salary)

# v1:int = 10
# obj_Person1: Person = Person("Aparna",25,50000)
obj_Person1 = Person("Aparna",25,50000)
# Aparna
# 25
# 50000
print()

obj_Person2: Person = Person("Vittal",26,50000)
# Vittal
# 26
# 50000
