# complex type - It is represented by complex class. It has a real part and an imaginary part 
# It is written as (real part)+(imaginary part)j
# Ex: 3+5j, here 3 is real part, 5j is imaginary part

c1 = 6+2j
# print('type of c1:',type(c1))
# type of c1: <class 'complex'>

# print(c1)
# (6+2j)

c2 = -5+12j
# print(c2)
# print(type(c2))
# (-5+12j)
# <class 'complex'>

# convert to complex number
x = 5
y = 10
m1 = complex(x,y)
print(m1)

# to fetch the real part from a complex number
r1 = m1.real
print(r1)
# 5.0

# to fetch the imaginary part from a complex number
img1 = m1.imag
print(img1)
# 10.0