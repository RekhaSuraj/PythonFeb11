# Print even numbers from 0 to 10

for v1 in range(0,11,2):
    print(v1)

# 0
# 2
# 4
# 6
# 8
# 10

for v in range(11):
    if v % 2 == 0:
        print(v)

# 0
# 2
# 4
# 6
# 8
# 10

print('************'*5)
# print odd numbers from 0 to 10
for v2 in range(11):
    if v2 %2 != 0:
        print(v2)

# 1
# 3
# 5
# 7
# 9

print('***even odd***')
# print even and odd numbers from 0 to 10
for m in range(11):
    if m % 2 == 0:
        print('even',m)
    elif m % 2 != 0:
        print('odd',m)

#
# even 0
# odd 1
# even 2
# odd 3
# even 4
# odd 5
# even 6
# odd 7
# even 8
# odd 9
# even 10

# Even odd numbers in separate lists
even_list=[]
odd_list = []
for i in range(11):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print('even list',even_list)
print('odd list',odd_list)

# even list [0, 2, 4, 6, 8, 10]
# odd list [1, 3, 5, 7, 9]

