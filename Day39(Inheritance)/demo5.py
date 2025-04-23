# Hierarchical Inheritance

# In Hierarchical inheritance, more than one child class is derived from a single parent class.
# In other words, we can say one parent class and multiple child classes.

class A:
    i = 10


class B(A):
    pass


class C(A):
    pass


obj_B = B()
print(obj_B.i)
# 10

obj_C = C()
print(obj_C.i)
# 10
