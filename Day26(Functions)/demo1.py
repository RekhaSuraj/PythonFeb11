# Functions :
# There are two types of functions :
# 1).Pre-defined functions
# Examples : print(),sum(),max(),min().........
# 2).User Defined Functions

# What is function ?
# Python Functions is a block of statements that return/perform the specific task.
# The idea is to put some commonly or repeatedly done tasks together and make a function
# so that instead of writing the same code again and again for different inputs, we can write in a 
# block of code

# To define user function by using def keyword

# def FunctionName():
#     statement...1
#     statement...2
#     statement...N
# FunctionName()

print('start here') #1
def new_function(): 
	print('Welcome to GRK') #3
	print('Welcome to procedural programming')

print('calling the function') #2
new_function()
print('outside of function')

print(type(new_function))
# <class 'function'>

# start here
# calling the function
# Welcome to GRK
# Welcome to procedural programming
# outside of function

# Function does nothing, will be implemented in the future
def function_name():
	pass


