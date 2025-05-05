# One try can have multiple except blocks
# In Python, an exception is an object derives from the BaseException class
# that contains information about an error
# In python  every error has a one class, when the runtime PVM(Python virtual machine) will create object of these classes

s1 = input('Enter a number')
s2 = input('Enter another number')

try:
    n1 = int(s1)
    n2 = int(s2)
    print(n1/n2)

except ZeroDivisionError as e:
    print(e,'occurred')

except ValueError as e:
    print(e,'occurred')

# general exception class
# except Exception as e:
#     print(e,'occurred')

else:
    print('No errors')

finally:
    print('Always gets executed')

# Normal termination
# Enter a number6
# Enter another number2
# 3.0
# No errors
# Always gets executed

# Graceful Termination: Zero division error
# Enter a number6
# Enter another number0
# division by zero occurred
# Always gets executed

# Giving an alphabet in the place of a number will give value error
# Enter a numbera
# Enter another number7
# invalid literal for int() with base 10: 'a' occurred
# Always gets executed