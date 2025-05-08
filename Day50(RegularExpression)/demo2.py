import re
# Regular Expression :
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern.

# Common re Functions
# Function	    Description
# re.match()	Matches pattern only at the start
# re.search()	Searches anywhere in the string
# re.findall()	Returns all matches as a list
# re.finditer()	Returns an iterator of matches
# re.sub()	Replaces matched patterns
# re.split()	Splits a string by the matched pattern


# RegEx : used for pattern matching or string matching.
#
# [abc]	a,b or c
# [^abc]	anycharacter except a,b or c
# [a-z]	lower case  a to z
# [A-Z]	Upper case  A to Z
# [a-zA-z] Both upper & lower case a to z and A to Z
# [0-9]	0 to 9


# syntax :
# ModuleName.method(pattern, string, flags= 0)

# Common Regex Patterns
# Pattern	Matches
# .	Any character except newline
# ^	Start of string
# $	End of string
# \d	Digit (0–9)
# \D	Non-digit
# \w	Word character (a-z, A-Z, 0–9, _)
# \W	Non-word character
# \s	Whitespace
# +	One or more
# *	Zero or more
# ?	Zero or one
# {n}	Exactly n times
# {n,}	At least n times
# {n,m}	Between n and m times
# [abc]	a or b or c
# [^abc]	Not a or b or c
# (abc)	Grouping
# `	`


# Special Sequences
# \A       Matches only at the start of the string.
#         \Z       Matches only at the end of the string.
#         \b       Matches the empty string, but only at the start or end of a word.
#         \B       Matches the empty string, but not at the start or end of a word.
#         \d       Matches any decimal digit; equivalent to the set [0-9] in
#                  bytes patterns or string patterns with the ASCII flag.
#                  In string patterns without the ASCII flag, it will match the whole
#                  range of Unicode digits.
#         \D       Matches any non-digit character; equivalent to [^\d].
#         \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
#                  bytes patterns or string patterns with the ASCII flag.
#                  In string patterns without the ASCII flag, it will match the whole
#                  range of Unicode whitespace characters.
#         \S       Matches any non-whitespace character; equivalent to [^\s].
#         \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
#                  in bytes patterns or string patterns with the ASCII flag.
#                  In string patterns without the ASCII flag, it will match the
#                  range of Unicode alphanumeric characters (letters plus digits
#                  plus underscore).
#                  With LOCALE, it will match the set [0-9_] plus characters defined
#                  as letters for the current locale.
#         \W       Matches the complement of \w.
#         \\       Matches a literal backslash.
