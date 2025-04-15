# Bitwise shift left <<
# Bitwise shift right >>

# Bitwise shift left - Shifts the position of the binary to left (according to the number of positions given)
# This adds the bits 
v1 = 4
print(v1<<1)
# 8

# 4 << 1 
#    	0 1 0 0 (4 in binary) 
# << 1  
# ---------------
#       1 0 0 0 (8 in binary)

# One more example
var1 = 5
print(var1 << 2)
#    0 0 0 1 0 1   (5 in binary)
# << 2
# ---------------
#    0 1 0 1 0 0   (20 in binary)



v2 = 24
print(v2<<2)
# 96


# Bitwise shift right - Shifts the position of the binary to right (according to the number of positions given)
# This looses the bits 
v3 = 5
print('shift right',v3>>1)
# shift right 1

print(8>>2)


#    0 1 0 1   (5 in binary)
# >> 1
# ---------------
#    0 0 1 0 --> (2 in binary, here we are loosing one bit)




