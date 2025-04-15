# List - Is a sequential datatype
# collection of elements, separated by commas (index separation is made using commas)
# it can be homogeneous or heterogeneous,
# each element is stored under a cell
# List is a mutable datatype(changeable)
# each cell has number--> index
# It can be declared within square brackets
# ALso it can be declared using a constructor

list1 = [10,20,30,40] #homogeneous 
print(type(list1))
# <class 'list

# Using constructor
l1 = list()
print(type(l1))
# <class 'list'>

list2 = [30.5,40,'hi',4+5j] #heterogeneous
print(list2)
# [30.5, 40, 'hi', (4+5j)]

# Each element will have a index number, it starts from 0
print(list1[0])
# 10

print(list1[3])
# 40

print(list2[2])
# hi
