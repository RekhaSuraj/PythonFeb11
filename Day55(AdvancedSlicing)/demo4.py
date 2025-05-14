import numpy as np

# 2d Advance slicing
a1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a1.ndim)
print(a1.shape)
print(a1)
# 2
# (3, 4)

#     c0  c1 c2 c3
# [r0[ 1  2  3  4]
#  r1[ 5  6  7  8]
#  r2[ 9 10 11 12]]

# Normal Slicing : [start : stop : step, start : stop : step]
print()
# Extract : [ 1  3  6  7 10 12]
print(a1[[0,0,1,1,2,2],[0,2,1,2,1,3]])

# hw - Extract [4 2 7 11 12 9 5]
