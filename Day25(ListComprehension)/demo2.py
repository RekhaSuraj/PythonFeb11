# List Comprehension

# List comprehension : Comprehension provides a shorter syntax, 
# to create a new list based on existing list.

# Using comprehension
# sy : [Expression for item in Iterable]
# Applied condition :
# sy : [Expression for item in iterable if condition]

# Print numbers from 0 to 10 in a list
list1 = []
for i in range(10):
	list1.append(i)

print(list1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension, the same code as above
list2 = [j for j in range(10)]
print(list2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]







