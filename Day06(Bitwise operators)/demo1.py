# Bitwise operators - 6 operators
# Bitwise & (Bitwise and)
# Bitwise | (Bitwise or)
# Bitwise XOR ^
# Bitwise not ~
# Bitwise shift left <<
# Bitwise shift right >>

# Bitwise & (and)
# Performs and operation on binaries
x = 5
y = 3
print(x&y)
# 1

# 5 --> 0  1  0  1
# 3 --> 0  0  1  1
# & --------------
#       0  0  0  1 - > 1

a = 4
b = 8
print(a&b)
# 0

# Bitwise | (or)
b1 = 6
b2 = 9
print('bitwise or:',b1|b2)
# 15

# 6 --> 0 1 1 0
# 9 --> 1 0 0 1
# | ------------
# 		1 1 1 1 --> 15
