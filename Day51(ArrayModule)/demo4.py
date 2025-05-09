import array
# unsigned integer - 'B'

# a1 = array.array('B',[-1,2,3])
# print(a1)
# OverflowError: unsigned byte integer is less than minimum

# a2 = array.array('B',[0,256])
# print(a2)
# OverflowError: unsigned byte integer is greater than maximum

a3 = array.array('B',[0,255,99])
print(a3)
# array('B', [0, 255, 99])