import re

details = 'Vittal age is 25, Aparna age is 24, Amar age is 30, Rama age is 200'

# print only names
n1 = re.findall(r'[A-Z][a-z]*',details)
print(n1)
# ['Vittal', 'Aparna', 'Amar', 'Rama']

# print ages 
n2 = re.findall(r'[0-9]{2}',details)

n3 = re.findall(r'[0-9]{2,3}',details)

print(n2)
# ['25', '24', '30', '20']
print(n3)
# ['25', '24', '30', '200']



