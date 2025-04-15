# The map(), filter() and reduce() functions bring a bit of functional programming to Python.
# All three of these are convenience functions that can be replaced with List Comprehensions 
# or loops,but provide a more elegant and short-hand approach to some problems.

# The map() Function
# The syntax is:
# The map() function iterates through all items in the given iterable and executes the function
# we passed as an argument on each of them.

# syntax: map(function, iterable(s))

# square all numbers in a list
list1 = [4,3,1,6,8,9]

def square_num(n):
	return n**2

# output as a list
v1 = list(map(square_num,list1))
print(v1)
# [16, 9, 1, 36, 64, 81]

v2 = tuple(map(square_num,list1))
print(v2)
# (16, 9, 1, 36, 64, 81)

# using lambda - hw