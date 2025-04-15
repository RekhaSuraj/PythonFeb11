l1 = [10,20]
l2 = [30,40]

l3 = [10,20,30,40]

print(l1+l2)
# [10, 20, 30, 40]


# syntax - append() Adds the element at the end of the list
l4 = [50,22,44,55]
l4.append(66)

print(l4)
# [50, 22, 44, 55, 66]

# copy - it creates a copy of the list into another list
list1 = [11,12,13,14,15]
list2 = list1.copy()
print('list2',list2)
# list2 [11, 12, 13, 14, 15]

# pop(index) - removes or deletes the element at the specified index
list3 = [22,33,44,55,66]
list3.pop(3)
print(list3)
# [22, 33, 44, 66]

# print(help(list))
# clear() - clears all the elements from the list and returns an empty list
li1 = [10,20,30]
li1.clear()
print(li1)
# []

