# Global Scope:
# Global variable
# A global variable is variable, which is defined outside the function,
# we access it anywhere in the function.

var1 = 'Vittal'
print(f'Global Var:{var1}')
def info():
	var2 = 'Aparna'
	print(f'Local Var:{var2}')
	print(f'Global Var:{var1}')


info()
print(f'Global Var:{var1}')
# Global Var:Vittal
# Local Var:Aparna
# Global Var:Vittal
# Global Var:Vittal

