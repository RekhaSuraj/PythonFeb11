# syntax:
# try:
#     # risky code
# except:
#     # recovery code#
# else:
#     # continue code#
# finally:
#     # cleanup code

# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

n1 = int(input('Enter a number'))
n2 = int(input('Enter another number'))

try:
    print(n1/n2) # risky code

except:
    print('Error occurred') # recovery code

print('Next line')

# Normal termination:
# Enter a number8
# Enter another number2
# 4.0
# Next line

# Graceful termination:
# Enter a number4
# Enter another number0
# Error occurred
# Next line
