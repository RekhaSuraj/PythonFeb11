fs1 = frozenset([102,103,104,105,'hi','hello'])
print(type(fs1))
# <class 'frozenset'>

# Return the union of sets as a new set.
# (i. e. all elements that are in either set.)
fs2 = frozenset(['mango','banana','orange','apple','grapes'])
fs3 = fs1.union(fs2)
print('fs3',fs3)
# frozenset({'hello', 'orange', 102, 103, 104, 105, 'banana', 'apple', 'hi', 'grapes', 'mango'})

# fs3.intersection()

# issubset() - Report whether another set contains this set.
fs4 = frozenset(['orange','apple'])
print(fs4.issubset(fs2))
# True


