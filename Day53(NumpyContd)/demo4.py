import numpy as np

nd1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(nd1)
# [      c0 c1 c2 c3
#     r0[ 1  2  3  4]
#     r1[ 5  6  7  8]
#     r2[ 9 10 11 12]
# ]

print(nd1[0])
# [1 2 3 4]

print(nd1[1])
# [5 6 7 8]

print(nd1[2])
# [ 9 10 11 12]

# fetch 2 from the above array
print(nd1[0][1])
# 2

#fetch 7
print(nd1[1][2])
# 7

print(sum([sum(nd1[0]),sum(nd1[1]),sum(nd1[2])]))
# 10 26 42
# 78