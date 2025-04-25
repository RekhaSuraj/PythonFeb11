# Method overloading - using multiple dispatch
# In Backend, Dispatcher creates an object which stores different implementation and on runtime,
# it selects the appropriate method as the type and number of parameters passed.
# Install multiple dipatch package
# Go to settings --> Select Project folder ---> Python Interpreter --> + (install package) ---> Multiple dispatch --> Install Package --> Finish
from multipledispatch import dispatch

class Arithmetic:

    @dispatch(int,int)
    def task(self,x,y):
        return x+y

    @dispatch(int,int,int)
    def task(self,x,y,z):
        return x+y*z

    @dispatch(int,int,int,int)
    def task(self,x,y,z,m):
        return x*y*z*m


ob1 = Arithmetic()
print(ob1.task(10,20))
# 30
print(ob1.task(3,5,6))
# 33
print(ob1.task(1,2,3,4))
# 24
