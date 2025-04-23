# Manager - Name, Age, Gender, NoOfTeams, Projects
# Employee - Name, Age, Gender, Technology

# Profile - Name, Age, Gender
# Parent class
class Profile:

    def __init__(self, Name, Age, Gender):
        self.name = Name
        self.age = Age
        self.gender = Gender


class Manager(Profile):

    def __init__(self,Name, Age, Gender, NoOfTeams, Projects):
        super().__init__(Name, Age, Gender)

        self.noOfteams = NoOfTeams
        self.projects = Projects


    def display(self):
        print(f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n No of Teams:{self.noOfteams}\n Projects:{self.projects}')


class Employee(Profile):

    def __init__(self, Name, Age, Gender, Technology):
        Profile.__init__(self,Name, Age, Gender)
        self.technology = Technology


    def display(self):
        print(f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n Technology:{self.technology}')



obj_Manager = Manager("Vittal",25,"Male",5,["Myntra","Flipkart","Amazon"])
obj_Manager.display()

# Name:Vittal
#  Age:25
#  Gender:Male
#  No of Teams:5
#  Projects:['Myntra', 'Flipkart', 'Amazon']

print()
obj_Employee = Employee("Amar",20,"Male","Python")
obj_Employee.display()

# Name:Amar
#  Age:20
#  Gender:Male
#  Technology:Python