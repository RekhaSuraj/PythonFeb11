# frozenset - read only set

# A frozenset in Python is an immutable version of a set. Once created, its elements cannot be changed,
# added, or removed.
# syntax: frozenset()
fs = frozenset([1, 2, 3, 4, 5])
print(fs)
print(type(fs))
# <class 'frozenset'>

# empty frozen set
fs1 = frozenset()
print(type(fs1))
# <class 'frozenset'>