class Person:
    Name = 'ABC'
    Gender = 'Female'
    Profession = 'Working'

print(type(Person()))
# <class '__main__.Person'>
# How do we create an object or instance of the class
obj_Person = Person()
print(obj_Person.Name)
print(obj_Person.Gender)
print(obj_Person.Profession)

print(type(obj_Person))
# <class '__main__.Person'>


