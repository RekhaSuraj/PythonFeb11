# Single level Inheritance

# In single level inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.
# Syntax : For inheritance, class B(A): - inside the round brackets give the class name which has to be inherited

class A:
    i = 10


class B(A):
    pass


obj_B = B()
print(obj_B.i)
# 10

