# Swap 2 variables without using 3rd variable

x = 10
y = 20

x = x + y #x=30
y = x - y #30-20 = 10
x = x - y #30-10 = 20

print('x:',x)
print('y:',y)
# x: 20
# y: 10

#In a single line
x1 = 10
x2 = 20
x1,x2 = x2,x1
print(x1,x2)
# 20 10