import numpy as np
n1 = np.array([1,2,3,4,5],dtype=float)
print(n1.dtype)
# float64
# print(n1)
# [1. 2. 3. 4. 5.]


# 2 dimension array matrix
n2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(n2)

# [
#   [ 1  2  3  4  5]
#   [ 6  7  8  9 10]
#  ]

print('Shape:',n2.shape)
print('Size:',n2.size)
print('NDim:',n2.ndim)
print('ItemSize:',n2.itemsize)

# Shape: (2, 5)
# Size: 10
# NDim: 2
# ItemSize: 8

# Reshape
n3 = n2.reshape(5,2)
print(n3)
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]]