# The filter() Function


# Similar to map(), filter() takes a function object and an iterable and creates a new list.

# As the name suggests, filter() forms a new list that contains only elements that 
# satisfy a certain condition,i.e. the function we passed returns True.

# The syntax is:

# filter(function, iterable(s))
# Print only even numbers from a list
list1= [2,3,5,4,6,7,9,10,11,14]

def even_num(num):
	return num%2 == 0


even_list = list(filter(even_num,list1))
print(even_list)

[2, 4, 6, 10, 14]

# using lambda
print(tuple(filter(lambda x:x%2==0,list1)))
# (2, 4, 6, 10, 14)


# odd numbers - hw
# print all items which start with 'A'

from functools import reduce
# reduce
list1 = [10,20,30,40,50]
res = reduce(lambda x,y:x+y, list1)
print(res)

# using for loop
sum1 = 0
for i in list1:
	sum1 = sum1+ i

print(sum1)


# using inbuilt sum
print(sum(list1))


