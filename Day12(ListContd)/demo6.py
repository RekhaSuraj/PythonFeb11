import sys
# tuple methods

# index () - Return first index of value
t1 = (11,22,44,'hello','hi',1,2,3,'hello')
print(t1.index('hello'))
# 3

print(t1.index(3))
# 7

# count() - Return number of occurrences of value.
print(t1.count('hello'))
# 2

print(t1.count(11))
#
# sys.getsizeof() - Return the size of object in bytes
list1 = [11,22,44,'hello','hi',1,2,3,'hello']
print('size of tuple',sys.getsizeof(t1))
print('size of list',sys.getsizeof(list1))

# size of tuple 112
# size of list 136

# Syntax Differences
# Feature	        List	                    Tuple
# Declaration	    my_list = [1, 2, 3]	        my_tuple = (1, 2, 3)
# Mutability	    Mutable (Changeable)	    Immutable (Unchangeable)
# Performance	    Slower (More Memory)	    Faster (Less Memory)
# Methods	        More(e.g., append(),
#                   remove())	                Fewer (Only count(), index())
# Use Cases	        When data changes often	    When data remains fixed