# Nested functions
# A nested function is a function defined inside another function

def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()  # Calling the inner function inside the outer function

outer_function()

# This is the outer function.
# This is the inner function.

def greet(name):
	
	def message():
		return f'Hello {name}'

	# message()

	return message()

var = greet('John')
print(var)



