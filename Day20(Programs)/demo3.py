# Factorial of a number
# factorial of 5 = 5*4*3*2*1 = 1*2*3*4*5

fact = 1
for i in range(1,6):
	print(i)
	fact = fact * i
	print('fact',fact)

print('Fatcorial of 5:',fact)


# Taking number from user
n = int(input('Enter the number to find factorial'))
fact = 1
for i in range(1,n+1):
	print(i)
	fact = fact * i
	print('fact',fact)

print(f"Factorial of {n}:{fact}")

