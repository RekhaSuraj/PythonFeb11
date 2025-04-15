# packing and unpacking
# packing - grouping into a single variable
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)

# ('apple', 'banana', 'cherry')
# unpacking - un grouping the tuple
# extract the values back into variables is called "unpacking":
(a,b,c) = fruits
print(a)
print(b)
print(c)
# apple
# banana
# cherry

x = (10,20,30)
print(x)
# (10, 20, 30)
(l,m,n) = x
print(l)
print(m)
print(n)
