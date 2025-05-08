import re
# check for match at the end of the string
s1 = 'This is the end'
# r'' - raw literal
# without r'
x1 = re.findall('end\\Z',s1)
print(x1)
# ['end']

# with r'
x2 = re.findall(r'end\Z',s1)
print(x2)
# ['end']

