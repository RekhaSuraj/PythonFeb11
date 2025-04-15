# Conversions
# Type casting
# Convert from int to complex() type
x = 10
y = 20
z = complex(x,y)
# print(z)
# 10+20j

# Implicit type casting - inbuilt casting from python
var1 = 20
var2 = 30.5

var3 = var1+var2
print(var3)
# 50.5
print(type(var3))
# <class 'float'>

# Explicit type casting
# Convert from int to float
a = 30
b = float(a)
# print(b)
# 30.0

# Convert from float to int
var4 = 50.45
f1 = int(var4)
# print(f1)
# 50

# COnvert from int to boolean
int1 = 32
b1 = bool(int1)
# print(b1)
# True

s1 = 'hello'
# n1 = int(s1)
# print(n1) 
# ValueError: invalid literal for int() with base 10: 'hello'

s2 = '10'
print(type(s2))
# <class 'str'>
n2 = int(s2)
print(n2)
print(type(n2))
# <class 'int'>




