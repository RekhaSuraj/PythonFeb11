# create an empty list
# using square brackets
list1 = []
print(list1)

# using constructor
list2 = list()
print(list2)

# list1.append(44,55)
# TypeError: list.append() takes exactly one argument (2 given)

# insert - inserts an element at the specified index
# syntax - insert(index, element)
l1 = [20,30,40,50]
l1.insert(2,35)
# print(l1)

# remove() - It will remove the element specified from the list
# syntax - remove(value)
l2 = [6,7,8,9,10]
# l2.remove(8)
# print(l2)

# l2.remove(11)
# ValueError: list.remove(x): x not in list

list1 = [1,2,3]
print(list1*2)