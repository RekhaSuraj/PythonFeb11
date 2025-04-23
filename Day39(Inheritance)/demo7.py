# Multiple Inheritance - with same variable names
# if both parents have same variable, only the first parent's will be considered.
# Here B class i value will be taken


class A:
    i = 10


class B:
    i = 20


class C(B,A):
    pass


obj_C = C()
print(obj_C.i)
# 20