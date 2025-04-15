# Simple calculator program

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

operation = input('Enter the operation to be performed')

if operation == '+':
	print(f'Addition of {num1} and {num2} is {num1+num2}')

elif operation == '-':
	print(f'Subtraction of {num1} and {num2} is {num1-num2}')

else:
	print('Invalid input')


# Multiplication
# Division
# Floor division
# MOdulus
# Exponentiation