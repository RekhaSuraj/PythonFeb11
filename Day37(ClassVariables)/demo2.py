# Update class level variables
class Electronics:
    Product = "Mobile" #class variable1
    Store = "Croma" #class variable2

    def __init__(self,Name,Price,RAM,Color):
        self.name = Name
        self.price = Price
        self.RAM = RAM
        self.color = Color

    def call_ClassVariable(self):
        print("Product Name:",Electronics.Product) #self.Product
        print("Store Name:",Electronics.Store) #self.Store



    def change_ClassVariable(self,new_Name):
        Electronics.Product = new_Name #or self.Product = new_Name


    def delete_ClassVariable(self):
        del self.Product

obj1 = Electronics("Samsung",20000,"6GB","White")
obj1.call_ClassVariable()
# Product Name: Mobile
# Store Name: Croma

# Updated the class variable to laptop
obj1.change_ClassVariable("Laptop")
print()
obj1.call_ClassVariable()
# Product Name: Laptop
# Store Name: Croma

# Delete class variable
obj1.delete_ClassVariable()

obj1.call_ClassVariable()
# AttributeError: 'Electronics' object has no attribute 'Product'

