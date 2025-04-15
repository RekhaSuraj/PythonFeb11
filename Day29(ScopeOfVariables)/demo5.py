
var1 = 100
def sum_function():
	var1 = 200
	print(f'Local Var:{var1}')
	print(globals()['var1'])
	sum1 = globals()['var1'] + var1
	print(sum1)


# sum_function()
# Local Var:200
# 100
# 300


v1 = 100
def function_test():
	v1 = 200
	print(f'Local Var:{v1}')
	print('Global Var Before update',globals()['v1'])
	globals()['v1'] = 2000
	print('Global Var After update',globals()['v1'])


print(globals()['v1']) #100

function_test()

print(globals()['v1'])
# 100
# Local Var:200
# Global Var Before update 100
# Global Var After update 2000
# 2000




