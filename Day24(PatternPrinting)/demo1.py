# Nested for loop - For every iteration of Outer loop, inner loop will complete its full iteration
for i in range(3):
	for j in range(3):
		print(j)


# i,j 0 0
# i,j 0 1
# i,j 0 2
# i,j 1 0
# i,j 1 1
# i,j 1 2
# i,j 2 0
# i,j 2 1
# i,j 2 2

ns1 = [[1,2,3],[4,5,6]]
for i in ns1:	
	for j in i:
		print('i',i)
		print('j',j)


# i [1, 2, 3]
# j 1
# i [1, 2, 3]
# j 2
# i [1, 2, 3]
# j 3
# i [4, 5, 6]
# j 4
# i [4, 5, 6]
# j 5
# i [4, 5, 6]
# j 6


list1 = [1,2,3,4,5,6]
for i in list1:
	print(i)





