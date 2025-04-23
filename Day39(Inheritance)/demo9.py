class Manager:

    def __init__(self, Name, Age, Gender, NoOfTeams, Projects):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.no0fTeams = NoOfTeams
        self.projects = Projects


    def diplay(self):
        print(f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n No of Teams:{self.no0fTeams}\n Projects:{self.projects}')



obj_Manager = Manager("Vittal",25,"Male",5,["Myntra","Flipkart","Amazon"])

obj_Manager.diplay()

# Name:Vittal
#  Age:25
#  Gender:Male
#  No of Teams:5
#  Projects:['Myntra', 'Flipkart', 'Amazon']

print()
class Employee:

    def __init__(self, Name, Age, Gender,Technology):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.technology = Technology


    def display(self):
        print(f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n Technology:{self.technology}')


obj_Employee = Employee("Amar",20,"Male","Python")
obj_Employee.display()

# Name:Amar
#  Age:20
#  Gender:Male
#  Technology:Python