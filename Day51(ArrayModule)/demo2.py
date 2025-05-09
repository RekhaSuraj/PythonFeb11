from array import array

a1 = array('i',[1,2,3,4,5])
print(type(a1))
print(a1.itemsize)
print(a1)
# array('i', [1, 2, 3, 4, 5])
# 4
# <class 'array.array'>

a2 = array('i',[1,2,3,4,5,6,2.0])
print(a2)
# TypeError: 'float' object cannot be interpreted as an integer
