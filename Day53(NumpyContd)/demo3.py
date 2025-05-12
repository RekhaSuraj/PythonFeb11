import numpy as np
# 2d array - From user

rows = int(input('Enter no of rows:'))
columns = int(input('Enter no of columns'))

a2 = np.ndarray(shape=[rows,columns],dtype=int)
for i in range(rows):
    for j in range(columns):
        a2[i][j] = int(input('Enter element'))

print(a2)


#    c0 c1 c2
# [r0[1 2 3]
#  r1[4 5 6]
#  r2[7 8 9]]

#     c0  c1 c2 c3
# [r0[ 1  2  3  4]
#  r1[ 5  6  7  8]
#  r2[ 9 10 11 12]]




