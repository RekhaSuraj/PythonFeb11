import array

import numpy as np

a1 = array.array('i',[1,2,3,4,5])
a2 = array.array('i',[5,6,7,8,9])

# zip() - The zip() function in Python aggregates elements from multiple iterables
# (like lists, tuples, or strings) into a single iterable of tuples. It pairs the i-th element
# from each input iterable into the i-th tuple in the output. The resulting zip object is an iterator,
# which can be converted to other data structures like lists or dictionaries.

# dot product
def prod_operation(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1 * v2
        # print(result)
    print('final result:',result)

# 115
prod_operation(a1,a2)

print(np.dot(a1,a2))
# 115
