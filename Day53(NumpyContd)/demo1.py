import array

import numpy as np
# What is an Array ?
# An array is basically a data structure which can be holds more than one value at a time.
# It is a collection or ordered series of elements of the same type

# Difference between numpyArray and list

# By default arrays concept is not available in python , instead of we can use list.
# [But, make sure list and Arrays both are not same]

# 1.But in python , we can create arrays in the following 2 ways
# How to import module?
# 1. By using array module
# 2. By using numpy Module

n1 = np.array([10,20,30,40,50,60])
print(type(n1))
# <class 'numpy.ndarray'>
print(n1)
# [10 20 30 40 50 60]


n2 = array.array('i',[1,2,3,4,5])
print(type(n2))
# <class 'array.array'>
print(n2)
# array('i', [1, 2, 3, 4, 5])