# index () - Returns the position(index value) of the element specified
list1 = [99,88,77,66,55,77]
print(list1.index(77))
# 2

# index() - with start index as a argument
print(list1.index(77,3))
# 5

# count(value) - Returns the number of occurrences of a value
print(list1.count(77))
# 2

print(list1.count(88))
# 1

# extend() - Adds 2 lists or appends 2 lists, here li2 is appended to li1
li1 = [10,20,30]
li2 = [50,60,70]

li1.extend(li2)
print(li1)
# [10, 20, 30, 50, 60, 70]
print(li2)
# [50, 60, 70]
