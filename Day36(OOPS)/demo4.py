
# Update instance variables using instance methods
class Employee:

    def __init__(self, Name, IdNum, Role, Technology):
        self.Name = Name
        self.IdNum = IdNum
        self.Role = Role
        self.Technology = Technology

    def display(self):
        print(f'Name {self.Name}')
        print(f'Id Number {self.IdNum}')
        print(f'Role {self.Role}')
        print(f'Technology {self.Technology}')


    def update(self):
        self.IdNum = 4567

    def capital_Name(self):
        self.Name = self.Name.upper()

    # delete a technology
    def delete_Technology(self):
        del self.Technology

obj_Employee1 = Employee("Vittal",12345,"Project Manager","Python")
obj_Employee1.display()

# Name Vittal
# Id Number 12345
# Role Project Manager
# Technology Python

print()
obj_Employee1.update()
obj_Employee1.display()

# Name Vittal
# Id Number 4567
# Role Project Manager
# Technology Python

print()
obj_Employee1.capital_Name()
obj_Employee1.display()

# Name VITTAL
# Id Number 4567
# Role Project Manager
# Technology Python

obj_Employee1.delete_Technology()
obj_Employee1.display()
# AttributeError: 'Employee' object has no attribute 'Technology'
