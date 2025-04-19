# Class variables
# Class Variables: A class variable is a variable that is declared inside of class,
# but outside of any instance method or __init__() method.

# Access class variables
# 1. <Class_Name.ClassVariable>
# 2. <self.ClassVariable>

class Student:
    # Class variable
    school = "Mahaveer Prakasham School"
    def __init__(self,Name,Age,Branch,Gender):
        self.s_Name = Name
        self.s_Age = Age
        self.s_Branch = Branch
        self.s_Gender = Gender


    def display(self):
        print(self.s_Name,self.s_Age,self.s_Branch,self.s_Gender)
        print(self.school) # class variable
        print(Student.school) #class variable



ob1 = Student("Aparna",25,"CS","Female")

ob2 = Student("Vittal","26","IEM","Male")

ob3 = Student("Rama",200,"Architecture","Male")

ob4 = Student("Seetha",300,"Development","Female")

all_objects = [ob1,ob2,ob3,ob4]

print(type(all_objects))
# <class 'list'>

for var in all_objects:
    print(var.s_Name)
    print(var.s_Age)
    print(var.s_Branch)
    print(var.s_Gender)
    print(var.school)
    print()

# Accessing class variable directly
print(ob1.school)

ob1.display()


