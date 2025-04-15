# Print all positive numbers in a pos_list and negative numbers in another list neg_list
list1 = [10,-20,40,-55,30,-35,-19,100,60.5]

num = 6
is_prime = False
for i in range(2,num):
	if num%i == 0:
		is_prime = False
		break
	else:
		is_prime = True


if is_prime == True:
	print('Prime')
else:
	print('Not prime')