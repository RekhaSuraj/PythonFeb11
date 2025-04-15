# lambda
# print(help('lambda'))
# lambda_expr/syntax  "lambda" [parameter_list] ":" expression

# Lambda expressions (sometimes called lambda forms) are used to create
# (nameless) functions. The expression "lambda parameters: expression"
# yields a function object.  The unnamed object behaves like a function
# object defined with:

# lambda expression to add 1 to a number
var1 = lambda a:a+1
print(type(var1))
# <class 'function'>

print(var1(4))
# 5

# lambda expression to add 2 numbers
var2 = lambda a,b:a+b
print(var2(2,6))
# 8

# lambda expression to multiply 2 numbers
var3 = lambda a,b:a*b
print(var3(11,12))
# 132


