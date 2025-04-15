# Write a program to take username, password from user and validate

user_name = input('Please enter username')
password = int(input('Please enter password'))

if user_name == 'python' and password == 1234:
    print('Access Granted')
else:
    print('Access Denied')

# Please enter usernamepython
# Please enter password1234
# Access Granted

# Please enter usernamepython
# Please enter password6789
# Access Denied

# Please enter usernamepython1
# Please enter password1234
# Access Denied


