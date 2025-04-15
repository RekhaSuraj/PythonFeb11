# Locals

def profile():
	Name = 'GRK'
	purpose = 'Training'
	Location = 'BTM'

	print(locals())
	print(locals()['purpose'])

profile()
# {'Name': 'GRK', 'purpose': 'Training', 'Location': 'BTM'}
# Training

# print(help(locals))

# locals()
#     Return a dictionary containing the current scope's local variables.

#     NOTE: Whether or not updates to this dictionary will affect name lookups in
#     the local scope and vice-versa is *implementation dependent* and not
#     covered by any backwards compatibility guarantees.