import re
# Email validation
email = input('Enter email')
# te.st34-7@test.com
pattern = r'[\w\.-]+@[\w\.-]+\.\w+$'
# [\w\.-]+@[\w\.-]+.\w'
if re.findall(pattern,email):
    print('Valid')
else:
    print('Invalid')

# Enter emailtest123@test.com
# Valid

# Enter emailtest_.25@test1.com
# Valid

# Enter email@test.com
# Invalid

# Enter emailtest@com
# Invalid