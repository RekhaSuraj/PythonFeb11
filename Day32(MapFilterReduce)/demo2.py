# reduce 
# reduce(function, sequence[, initial])
# reduce() works by calling the function we passed for the first two items in the sequence. 
# The result returned by the function is used in another call to function alongside with the 
# next (third in this case), element.

from functools import reduce
# syntax: reduce(function, iterable [, initial])

# function: A function that takes two arguments.
# iterable: A sequence (like a list).
# initializer (optional): A value that is used as the initial value.

list1 = [10,20,30,40,50,60]

# (((10+20)+30)+40)

def sum_num(a,b):
	return a+b

res = reduce(sum_num,list1)
print(res)

res1 = reduce(lambda x,y:x+y,list1)
print('using lambda',res1)


# How it works:
# reduce() applies the lambda function cumulatively to the items of the list.

# First it does: 10 + 20 → 30

# Then: 30 + 30 → 60

# Then: 60 + 40 → 100

# Then: 100 + 50 → 150

# Then: 150 + 60 → 210


# using lambda 

# normal methods
sum1 = 0
for i in list1:
	sum1 = sum1+i

print(sum1)

# inbuilt sum method
print(sum(list1))

# product/multiplication of all items in the list using reduce - hw