# Print all negative numbers into a new list
list1 = [10,20,-40,50,-60,70,-90]

# neg_list = []
# for l in list1:
# 	if l < 0:
# 		neg_list.append(l)

# print(neg_list)
# [-40, -60, -90]

# list comprehension

l1 = [m for m in list1 if m<0]
print(l1)
# [-40, -60, -90]


l2 = [m for m in list1 if m>0]
print(l2)
# [10, 20, 50, 70]

list1 = []
for i in range(10):
	if i % 2 ==0:
		list1.append(i)

print(list1)

# [0, 2, 4, 6, 8]

li1 = [i for i in range(10) if i %2 == 0]
print(li1)

odd_list = [i for i in range(10) if i %2 != 0]
print(odd_list)
# [0, 2, 4, 6, 8]

s_list = []
for i in range(5):
	s_list.append(i**2)

print(s_list)
# [0, 1, 4, 9, 16]

l_c = [i**2 for i in range(5)]
print(l_c)
# [0, 1, 4, 9, 16]

list1 = [22,10,33,44,55]
l1 = [n+1 for n in list1]
print(l1)
# [23, 11, 34, 45, 56]



