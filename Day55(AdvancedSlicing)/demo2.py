# Slicing 3-D

#     i   ,    j   ,  c
# [[[],[]],[[],[]],[[],[]]]

# syntax : [start : stop : step, start : stop : step, start : stop: step]
import numpy as np

d1 = np.array([[[1,2,3,4,5],[5,6,7,8,9]],[[9,10,11,12,13],[14,15,16,17,18]]])
print('Shape:',d1.shape)
print('Dimension:',d1.ndim)
print('Size:',d1.size)
print(d1)

# Shape: (2, 2, 5)
# Dimension: 3
# Size: 20

#            c0 c1 c2 c3 c4
# [i0-->[j0[ 1  2  3  4  5]
#       j1 [ 5  6  7  8  9]]
#
#  i1-->[j0[ 9 10 11 12 13]
#       j1 [14 15 16 17 18]]]

print()
# [[[1 2 3 4 5]]]
print(d1[0:1,0:1,::])

print()
# [[[10 11 12]
#   [15 16 17]]]
print(d1[1::,::,1:4])


print()
# [[[ 1  5]
#   [ 5  9]]
#
#  [[ 9 13]
#   [14 18]]]
print(d1[::,0::,0::4])

# hw -