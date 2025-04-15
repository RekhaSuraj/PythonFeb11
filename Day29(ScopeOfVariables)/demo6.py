# Enclosing scope

# Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. 
# If the local scope is an inner or nested function, then the enclosing scope is the scope of the 
# outer or enclosing function. 
# This scope contains the names that you define in the enclosing function. 
# The names in the enclosing scope are visible from the code of the inner and enclosing functions.


# Enclosing variable declared Inside the outer function,Outside the inner function

x = 10 # Global Var
def outer_function():
	var1 = 100 # Enclosed var

	def inner_function():
		var2 = 200
		print(f'Local Var: {var2}')
		print(f'Enclosed Var: {var1}')


	inner_function()
	print('Enclosed Var after inner_function:', var1)

 
outer_function()

# Local Var: 200
# Enclosed Var: 100
# Enclosed Var after inner_function: 100


