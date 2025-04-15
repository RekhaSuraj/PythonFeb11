#Chain multiple if statement in Python
# In Python, the if-elif-else condition statement has an elif blocks to chain multiple conditions one after another. This is useful when you need to check multiple conditions.
#
# With the help of if-elif-else we can make a tricky decision. The elif statement checks multiple conditions one by one and if the condition fulfills, then executes that code.
#
# Syntax of the if-elif-else statement:
#
# if condition-1:
#      statement 1
# elif condition-2:
#      stetement 2
# elif condition-3:
#      stetement 3
#      ...
# else:
#      statement

# In the above example, the elif conditions are applied after the if condition.
# Python will evalute the if condition and if it evaluates to False then it will evalute
# the elif blocks and execute the elif block whose expression evaluates to True.
# If multiple elif conditions become True, then the first elif block will be executed.


Day = int(input('Enter a number'))
if Day == 1:	# False
	print('Is is Sunday')

elif Day == 2:
	print('It is Monday') # True

elif Day ==3:
	print('It is Tuesday')

elif Day == 4:
	print('It is Wednesday')

elif Day == 5:
	print('It is Thursday')

elif Day == 6:
	print('It is Friday')

elif Day == 7:
	print('It is Saturday')

else:
	print('Invalid Input')

# Enter a number2
# It is Monday

# Enter a number0
# Invalid Input

