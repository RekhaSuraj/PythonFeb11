# Write a program to check if a number is Prime number or not

n1 = int(input('Please enter a number'))
is_Prime = False
for i in range(2,n1):
    if n1 % i == 0:
        is_Prime = False
        break
    else:
        is_Prime = True


if is_Prime == True:  # if is_Prime
    print(n1,'is a prime number')

else:
    print(n1,'is not prime')


# 7 %2 not 0 , else -is_Prime =  True
# 7%3 not 0  else -is_Prime =  True
# 7%4 not 0 else is_Prime =  True
# 7%5 not 0 else is_Prime =  True
# 7%6 not 0 else is_Prime =  True


# Please enter a number5
# 5 is a prime number

# Please enter a number8
# 8 is not prime





