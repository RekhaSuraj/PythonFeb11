import numpy as np
l1 = [1,2,3,4,5,6,7]

# print(l1 > 3)
# TypeError: '>' not supported between instances of 'list' and 'int'

s1 = np.array([1,2,3,4,5,6,7])
print(s1+1)
# [2 3 4 5 6 7 8]

print(s1*2)
# [ 2  4  6  8 10 12 14]

# Returns in bool
print(s1 > 3)
# [False False False  True  True  True  True]

# To print values greater than 3
print(s1[s1 > 3])
# [4 5 6 7]


