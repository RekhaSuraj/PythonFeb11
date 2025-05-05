n1 = int(input('Enter a number'))
n2 = int(input('Enter another number'))

try:
    print(n1/n2) # risky code

except ZeroDivisionError as error:
    print('Error occurred') # recovery code
    print(error, 'in divide method, class_name has occurred')

print('Next line')

# Enter a number8
# Enter another number0
# Error occurred
# division by zero in divide method, class_name has occurred
# Next line