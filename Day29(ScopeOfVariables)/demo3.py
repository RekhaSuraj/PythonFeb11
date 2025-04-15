# Taking same name for global and local variable

var1 = 'Test'
def profile():
	var1 = 'inside_Test'
	print(f'Local Var:{var1}')
	print('Global Var',globals()['var1'])


profile()
# Local Var:inside_Test
# Global Var Test

# print(help(globals))
# Return the dictionary containing the current scope's global variables.

#     NOTE: Updates to this dictionary *will* affect name lookups in the current
#     global scope and vice-versa.