# Write a program to print first 5 even numbers

i = 0
even_cntr = 0
while even_cntr < 5:
	if i % 2 == 0:
		print(i)
		even_cntr = even_cntr + 1
		# print('evencntr',even_cntr)

	i = i + 1
	# print(i)

print('after while loop')

# 0
# 2
# 4
# 6
# 8

# Write a program to print first 15 odd numbers - hw