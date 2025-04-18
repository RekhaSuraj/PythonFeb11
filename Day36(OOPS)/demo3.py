# Calling Instance Variables by using Instance method
# Instance method: Used to access or modify the object state. If we use instance variables inside a method,
# such methods are called instance methods. It must have a self parameter to refer to the current object.

class Mobile:

    def __init__(self,Name, RAM, Color, Price, Mfg):
        self.m_Name = Name
        self.m_RAM = RAM
        self.m_Color = Color
        self.m_Price = Price
        self.m_Mfg = Mfg

    # Instance method: Has instance variables
    def display(self):
        print(f'Name: {self.m_Name}')
        print(f'RAM: {self.m_RAM}')
        print(f'Color: {self.m_Color}')
        print(f'Price:{self.m_Price}')
        print(f'ManufactureYear:{self.m_Mfg}')


obj_Samsung = Mobile("Samsung",8,"White",30000,2025)
# Calling instance method
obj_Samsung.display()

# Name: Samsung
# RAM: 8
# Color: White
# Price:30000
# ManufactureYear:2025






