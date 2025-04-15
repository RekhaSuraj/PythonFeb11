# To calculate the percentage from the input given by the users

num1 = eval(input('Enter the first subject marks'))
num2 = eval(input('Enter the second subject marks'))
num3 = eval(input('Enter the third subject marks'))
num4 = eval(input('Enter the fourth subject marks'))
num5 = eval(input('Enter the fifth subject marks'))

total_marks = num1+num2+num3+num4+num5
print('total marks',total_marks)

percentage = (100*total_marks)/500
print('Percentage',percentage)

# Enter the first subject marks99
# Enter the second subject marks100
# Enter the third subject marks98
# Enter the fourth subject marks97
# Enter the fifth subject marks100
# total marks 494
# Percentage 98.8