v1 = [22,12,'hello','hi',[[10,20,30],40,50,60,70],80,'a',['b','c']]

print('index of 0:',v1[0])
print('index of 1:',v1[1])
print('index of 2:',v1[2])
print('index of 3:',v1[3])
print('index of 4:',v1[4])
print('index of 5:',v1[5])
print('index of 6:',v1[6])
print('index of 7:',v1[7])

# index of 0: 22
# index of 1: 12
# index of 2: hello
# index of 3: hi
# index of 4: [[10, 20, 30], 40, 50, 60, 70]
# index of 5: 80
# index of 6: a
# index of 7: ['b', 'c']

# print 30
print(v1[4][0][2])
# 30

# print b
print(v1[7][0])
# b

# print [10,20,30] using slicing
print(v1[4][0:1])

# [10, 20, 30], 40,
print(v1[4][0:2])
# [[10, 20, 30], 40]

# assignment
l2 = [1,2,['a',2,[3],5,6],[3,'d','r','t','d',[[11,22,33],[12,13,14],[34,56,78],11,12,13],'abc'],'python','java']

# print 12

# print 22

# [2,[3],5,6] using slicing

str1 = 'hi'


