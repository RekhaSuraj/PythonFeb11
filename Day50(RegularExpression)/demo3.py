import re
# sy : re.FunctionName(pattern,string)

# match  : It checks at the beginning of the string

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern.

x1 = 'My name is devi'

v1 = re.match("My",x1)
print(v1)
# <re.Match object; span=(0, 2), match='My'>
print(v1.group())
# My

v2 = re.match('is',x1)
print(v2)
# None