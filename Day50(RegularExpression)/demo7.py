import re
# mobile number
# MobileNumber : India Mobiles number should starts with 6,7,8 or 9
# [6789][0-9]{9}
# Number startswith: 789
# [789][0-9]{9}

num1 = input('Enter a number')
if re.findall(r'[789][0-9]{9}',num1):
    print('Valid')
else:
    print('Invalid')

# Enter a number7656785432
# Valid

# Enter a number6567893456
# Invalid

# Enter a number890675
# Invalid