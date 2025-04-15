# find() - Gives the index position of the character specified
# find(): If the substring is found, it returns the index of the first occurrence.
# If the substring is not found, it returns -1.
str1 = 'Mangoes are sweet'
res = str1.find('o')
print(res)

# occurrence of letter e
res1 = str1.find('e',6, 11)
print(res1)
# 10

res2 = str1.find('e',12)
print(res2)
# 14

# startswith() - Checks if the start letter or character starts with the specified prefix(sub)
str3 = 'Aparna'
print(str3.startswith('a'))
# False

print(str3.startswith('A'))
# True

print('-----ends with----')
str4 = 'Python Monday'
print(str4.endswith('y'))
# True

print(str4.endswith('n',0,6))
# True



