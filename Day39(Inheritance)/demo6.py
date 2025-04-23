# Multiple Inheritance

# Multiple Inheritance
# In multiple inheritance, one child class can inherit from multiple parent classes.
# So here is one child class and multiple parent classes.

class A:
    i = 20


class B:
    j = 30


class C(A,B):
    pass

obj_C = C()
print(obj_C.i)
print(obj_C.j)

# 20
# 30