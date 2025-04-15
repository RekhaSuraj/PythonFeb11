# Write a program for taking pwd input from user, if wrong pwd for 3 attempts, then account gets locked

num1 = int(input('Please enter password'))
attempts = 1
while attempts <3:
    if num1 == 1234:
        print('Correct Password')
        break
    else:
        print('Incorrect password')
        num1 = int(input('Please enter password once again'))

    attempts += 1
    # print(attempts)

else:
    print('Account locked')

# Please enter password768
# Incorrect password
# Please enter password once again1234
# Correct Password

# Please enter password656
# Incorrect password
# Please enter password once again656
# Incorrect password
# Please enter password once again35
# Account locked










