import numpy as np

l1 = [1,2,3,4,5,6,7,8,9]
# syntax: [start:stop:step]

a1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(a1.ndim)
print(a1.shape)
print(a1.size)
print(a1)
# 2
# (3, 5)
# 15
#      c0 c1 c2 c3 c4
# [r0[ 1  2  3  4  5]
#  r1[ 6  7  8  9 10]
#  r2[ 11 12 13 14 15]]


# Two dimensional slicing :
# sy : [rows_slicing, columns_slicing]
# [start : stop : step , start : stop : step]

# [[1 2
#  6 7
#  11 12]]
# print(a1[0::,0:2])
print(a1[::,:2])

print()
# [[2 3
#   7 8
#   12 13]]
print(a1[::,1:3])

print()
# [[9 10
#   14 15]]

print(a1[1::,3:])
# [[ 9 10]
#  [14 15]]

print()
print(a1[1::,1:3])
# [[ 7  8]
#  [12 13]]

#      c0 c1 c2 c3 c4
# [r0[ 1  2  3  4  5]
#  r1[ 6  7  8  9 10]
#  r2[ 11 12 13 14 15]]


print()
# [[1 3
#   6 8
#   11 13]]
print(a1[0::,:3:2])

