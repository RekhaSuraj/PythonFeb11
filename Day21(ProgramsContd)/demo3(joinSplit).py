# join () - # The string whose method is called is inserted in
# between each given string. The result is returned as a new string.
str2 = 'Hello World'
str3 = '.'.join(str2)

print(str3)
# H.e.l.l.o. .W.o.r.l.d

str4 = '&'.join(str2)
print(str4)
# H&e&l&l&o& &W&o&r&l&d

# split() - Return a list of the substrings in the string, using sep as the separator string
# If nothing is specified inside the split() method, it will take space as a separator by default
s1 = 'Today is a Good Day'
s2 = s1.split()
print(s2)
# ['Today', 'is', 'a', 'Good', 'Day']

# sep -
# The separator used to split the string.
# When set to None (the default value), will split on any whitespace character (including and spaces) and will discard
#   empty strings from the result.
# If we specify a separator inside split(), it will create the list based on that separator
s3 = 'Today-is-a-good-day'
s4 = s3.split('-')
print(s4)





