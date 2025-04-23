# Hybrid Inheritance

# When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.

class A:
    i = 10


class B(A):
    j = 20


class C(A):
    k = 30


class D(B,C):
    pass

obj_D = D()
print(obj_D.i)
print(obj_D.j)
print(obj_D.k)

# 10
# 20
# 30