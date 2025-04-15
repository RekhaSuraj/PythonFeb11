str1 = 'Python'

# isdigit() - Checks to see if a string contains only digits(numbers)
print(str1.isdigit())
# False

str2 = '12345'
print(str2.isdigit())
# True

str3 = '3456*%'
print(str3.isdigit())
# False

# Return True if the string is an alphabetic string, False otherwise.
# A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string
str4 = 'Developer'
print(str4.isalpha())
# True

str5 = 'Hello World'
print(str5.istitle())
# True

print(str5.isalpha())
# False

# Return a copy with all occurrences of substring old replaced by new.
# Replaces the old value with the new one
s1 = str5.replace("o","Q")
print(s1)
# HellQ WQrld

s2 = str5.replace(" ","")
print(s2)
# HelloWorld

# lstrip() - Return a copy of the string with leading whitespace removed
# Removes spaces from the start
s2 = '   Welcome'
s3 = s2.lstrip()
print(s3)
# Welcome

# rstrip() - Return a copy of the string with trailing whitespace removed.
s4 = 'Welcome '
# print(s4)
s5 = s4.rstrip()
print(s5)
# Welcome

# strip() - Return a copy of the string with leading and trailing whitespace removed.
v1 = " Hello  World    Welcome to Class   "
v2 = v1.strip()
print(v2)
# Hello  World   Welcome to Class

print(v2.replace(" ",""))
# HelloWorldWelcometoClass











