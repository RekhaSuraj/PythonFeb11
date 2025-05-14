import numpy as np

a1 = np.array([1,2,3,4,5,6,7,8,9,10])

# 1-D slicing
# [start : stop : step]  ---> Order Sequence
# What is Arbitrary ?
# To get values without using slicing , It means There is no order.
# 1,2,4,5,7,10

s1 = np.array([0,1,3,4,6,9])
print(a1[s1])
# [ 1  2  4  5  7 10]

