# slicing start:stop:step

l1 = ['hello','hi',22,'welcome',33,44,'python',55]

# print welcome using indexing
print(l1[3])
# welcome

# using slicing
print(l1[3:4])
# ['welcome']

# print 44,'python'
print(l1[5:7])
# [44, 'python']

print(l1[-1])
# 55

# print entire list in reverse order using slicing
print(l1[::-1])
# [55, 'python', 44, 33, 'welcome', 22, 'hi', 'hello']

# empty list
print(l1[-2:-4])
# []

# 44, python using -ve slicing
print(l1[-3:-1])
# [44, 'python']