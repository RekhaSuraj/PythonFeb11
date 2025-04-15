# Logical operators
# There are 3 logical operators - and, or , not
# Returns a Boolean value
# Returns True only if both values are True
# Even if one value is False, it returns False

# syntax - and
print(True and False)
# False

print(True and True)
# True

print(False and True)
# False

print(False and False)
# False

print(10 and 20)
# 20

print(10 and -15)
# -15

# or operator 
# syntax - or
# Returns True if atleast one value is True
# Returns False only if both values are False

print(True or False)
# True

print(False or True)
# True

print(False or False)
#False

print(True or True)
# True

# not opearotor - reverses or gives opposite result of inner operation
# syntax not()
print(not(True or True))
# False

print(not(True and False))
# True

print(not(False and False))
# True
