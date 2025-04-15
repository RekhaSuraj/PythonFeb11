# Nested list - Lists placed inside of lists

l1 = [11,22,33,44,['a','b','c'],19,20,21,22,[33,10,11,12],[1,2],3,4]

print(len(l1))
# 13

print('index of 0:',l1[0])
print('index of 1:',l1[1])
print('index of 2:',l1[2])
print('index of 3:',l1[3])
print('index of 4:',l1[4])
print('index of 5:',l1[5])
print('index of 6:',l1[6])
print('index of 7:',l1[7])
print('index of 8:',l1[8])
print('index of 9:',l1[9])
print('index of 10:',l1[10])
print('index of 11:',l1[11])
print('index of 12:',l1[12])

# index of 0: 11
# index of 1: 22
# index of 2: 33
# index of 3: 44
# index of 4: ['a', 'b', 'c']
# index of 5: 19
# index of 6: 20
# index of 7: 21
# index of 8: 22
# index of 9: [33, 10, 11, 12]
# index of 10: [1, 2]
# index of 11: 3
# index of 12: 4

# print('index of 13:',l1[13])
# IndexError: list index out of range