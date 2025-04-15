# set methods
set1 = {11,22,3,44,55,6,77,8}

# add() - adds an element to a set
set1.add(100)
print(set1)
# {3, 100, 6, 8, 11, 44, 77, 22, 55}

# duplicates are not inserted, but does not throw error
set1.add(100)
print(set1)

# print(help(set))
# pop() - Remove and return an arbitrary(random) set element
print(set1.pop())
# 3 element which is deleted(poped)
print(set1)

# Raises KeyError if the set is empty.
# set2 = set()
# set2.pop()
# KeyError: 'pop from an empty set'

