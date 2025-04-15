list1 = []
for i in range(10):
	list1.append(i)

print(list1)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = []
odd_list = []
for i in range(11):
	if i % 2 == 0:
		even_list.append(i)
	else:
		odd_list.append(i)	

print(even_list)
print(odd_list)

# [0, 2, 4, 6, 8, 10]
# [1, 3, 5, 7, 9]

