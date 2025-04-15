# To pass Parameters when you defining function

# syntax : def functionname(para1,para2,........ParaN):
#                 body of function
#
#         functionname(Arg1,Arg2,...........AgrN)

# Passing parameters to a method, all parameters must be sent by default
def profile(name,age,salary):
	print(f'Name:{name}')
	print(f'Age:{age}')
	print(f'Salary:{salary}')


# profile()
# TypeError: profile() missing 3 required positional arguments: 'name', 'age', and 'salary'

profile('vittal',25,50000)

# Name:vittal
# Age:25
# Salary:50000

# profile('vittal',25)
# TypeError: profile() missing 1 required positional argument: 'salary'


# profile('vittal')
# TypeError: profile() missing 2 required positional arguments: 'age' and 'salary'
