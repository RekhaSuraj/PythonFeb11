# Simple ATM program

balance = 1000
amount = int(input('Please enter the amount to be withdrawn'))

if amount > balance:
	print('Insufficient balance')

else: 
	balance = balance - amount
	print('Your current balance is: ',balance)


# Please enter the amount to be withdrawn200
# Your current balance is:  800

# Please enter the amount to be withdrawn2000
# Insufficient balance
