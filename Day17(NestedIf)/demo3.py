# Nested if 
# In Python, the nested if-else statement is an if statement inside another if-else statement. 
# It is allowed in Python to put any number of if statements in another if statement.
#
# Indentation is the only way to differentiate the level of nesting. 
# The nested if-else is useful when we want to make a series of decisions.
#
# Syntax of the nested-if-else:
#
# if conditon_outer:
#     if condition_inner:
#         statement of inner if
#     else:
#         statement of inner else:
#     
# else:
#     Outer else
# statement outside if block

# n1 = int(input('Please Enter a number'))

# if n1 > 0:
# 	if n1 % 2 == 0:
# 		print('Even number')
# 	else:
# 		print('Odd number')

# else:
# 	print('Inavlid input')


# Please Enter a number6
# Even number

# Please Enter a number0
# Inavlid input

# Please Enter a number-45
# Inavlid input

# Please Enter a number9
# Odd number

# ANother method to do the same progrm

n1 = int(input('Enter a number'))
if n1 < 0:
	print('Invalid input')

else:
	if n1 % 2 == 0:
		print('Even number')
	else:
		print('Odd number')


# Enter a number-2
# Invalid input

# Enter a number4
# Even number


