# Factorial of a number

def factorial(num):
	fact = 1
	for i in range(1,num+1):
		fact = fact*i

	return fact


a = factorial(5)
print(a)
# 120

print('***********')
def return_example():
	return 'Hello from GRK'


var1 = return_example()
print(var1)
# Hello from GRK

print('***********')
# Prime number using functions
def is_Prime(num):
	msg = True

	for i in range(2,num):
		if num%i == 0:
			msg = False
			break

		else:
			msg = True

	return msg

n1 = int(input('Enter a number'))
v = is_Prime(n1)

if v:
	print('Prime number',n1)
else:
	print('Not a prime number',n1)


# Enter a number4
# Not a prime number 4


# Enter a number7
# Prime number 7




