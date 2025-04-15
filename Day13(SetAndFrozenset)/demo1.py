# set 
# Set is an unordered collection of unique elements, set does not support index
# set is declared inside flower braces
# insertion order is not preserved, does not allow duplicates
# Mutable: You can modify a set by adding or removing elements (add(), remove(), discard(), pop(), clear()).
# Elements Must Be Immutable: You cannot have lists or other sets as elements in a set because they are
# not hashable.

# set is declared using flower(curly) braces

s1 = {10,20,30,40,50}
print(type(s1))
# <class 'set'>

# empty flower braces will create an empty dictionary
s2 = {}
print(type(s2))
# <class 'dict'>

# creating an empty set using constructor
s3 = set()
print(type(s3))
# <class 'set'>

s4 = set({11,22,33,44})
print(s4)
print(type(s4))
# <class 'set'>