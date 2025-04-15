# Write a program to reverse a string using while loop

str1 = 'Have a good day'

# Write a program to reverse a number using while loop

num1 = int(input('Please enter a number'))
rev_num = 0
while num1 != 0:

	rem = num1 % 10 
	print('rem',rem)
	rev_num = (rev_num * 10) + rem
	print('rev_num',rev_num)
	num1 = num1 // 10
	print('num1',num1)

print(rev_num)

# Please enter a number4567
# 7654