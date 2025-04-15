# Identity operators 
# These also are used only for iterables 
# There are 2 types - is, is not

# is - checks to see if both objects are the same or not. Returns True if both are same object
list1 = [10,20,30]
list2 = [10,20,30]

# print(list1 is list2)
# False

# id(obj) - an inbuilt method to fetch the address of an object
# syntax : id(obj)
# print(id(list1))
# 1396804407680

# print(id(list2))
# 2955906046144

list3 = list1
# print(list1 is list3)

# print(id(list3))
# 2564171682176

# is not - Oppositr of is
list3 = [50,65,75,85]
list4 = [50,65,75,85]

# print(list3 is not list4)
# True

# string
str1 = 'hello'
str2 = 'hello'
print(str1 is str2)

print(id(str1))
print(id(str2))
# True

print(str1 is not str2)
# False

n1 = 10
n2 = 10
print(n1 is n2)

print(id(n1))
print(id(n2))

