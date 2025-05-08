import re

# check for a single digit
s1 = 'Vittal age 22 vittal@452223 6786 22224'

sd = re.findall(r'\d',s1)
print(sd)
# ['2', '2', '4', '5', '2', '2', '2', '3', '6', '7', '8', '6']

# check for double digit
dd = re.findall(r'\d{2}',s1)
print(dd)
# ['22', '45', '22', '23', '67', '86']

# check for number 2 - for 2 or more occurrences
x2 = re.findall(r'[2]{2,}',s1)
print(x2)
# ['22', '222', '2222']

# other than number 2
r1 = re.findall(r'[^2]',s1)
print(r1)
# ['V', 'i', 't', 't', 'a', 'l', ' ', 'a', 'g', 'e', ' ', ' ', 'v', 'i', 't', 't', 'a', 'l', '@', '4', '5', '3', ' ', '6', '7', '8', '6', ' ', '4']