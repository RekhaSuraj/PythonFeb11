# LEGB Rules
# Local rule : Firstly, it check within that self, if the value doesn't find within that self it will go 
# up next scope. It follows LEGB hierarchy(order)


# def greet():
# 	prod = 'phone'
# 	print(prod)


# greet()


prod = 'mobile'
def greet():
	prod = 'landline'
	print(prod)


greet()
print(prod)
