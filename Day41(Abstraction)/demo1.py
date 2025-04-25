# Method overloading
# Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.
# These methods are called overloaded methods and this is called method overloading.
class cls_Overload:

    def add(self,x,y,z=0,m=0):
        return x+y


    def add(self,x,y,z=0,m=0):
        return x+y+z


    def add(self,x,y,z=0,m=0):
        return x+y+z+m


ob1 = cls_Overload()
print(ob1.add(5,6,1,2))
print(ob1.add(4,10))