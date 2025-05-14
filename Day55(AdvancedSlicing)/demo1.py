import numpy as np
# 3d - Numpy Array

n1 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

print(n1.ndim)
print(n1.shape)
print(n1.size)

print(n1)
# 3
# (3, 2, 3)
# 18

#           c0  c1  c2
# [i0-->[j0[ 1  2  3]
#       j1 [ 4  5  6]]
#
#  i1-->[j0[ 7  8  9]
#        j1 [10 11 12]]
#
#  i2-->[j0[13 14 15]
#        j1[16 17 18]]]

print(n1[0][0][1])
# 2

print(n1[2][1][2])
# 18