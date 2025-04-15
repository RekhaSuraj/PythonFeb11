# Type conversion or type casting

# convert from list to tuple
list1 = [10,20,30,50,60]
print('before conversion',type(list1))
print(list1)
# before conversion <class 'list'>
t1 = tuple(list1)
print('after conversion',type(t1))
# after conversion <class 'tuple'>
print(t1)


# convert from tuple to list
t1 = (11,22,33,44,55,'hi','hello')

print('before conversion',t1)
# before conversion (11, 22, 33, 44, 55, 'hi', 'hello')
l1 = list(t1)
print(type(l1))
# <class 'list'>
print('after conversion',l1)
# after conversion [11, 22, 33, 44, 55, 'hi', 'hello']
print(type(t1))
# <class 'tuple'>

# Conversion from list to set
l1 = [20,30,40,50,10,20,30]
s1 = set(l1)
# print(s1)
# {40, 10, 50, 20, 30}

# conversion from set to list
s2 = {11,25.6,30.5,'hi','hello'}
li1 = list(s2)
print(li1)
# [30.5, 'hello', 11, 'hi', 25.6]




