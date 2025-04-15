v1 = 10
print('GV',v1)
def outer_fn():
	global v1
	v1 = 20
	print('EV',v1)
	def inner_fn():
		global v1 
		v1 = 30
		print('LV',v1)

	print('before inner_fn call',v1)
	inner_fn()
	print('after inner_fn call',v1)


outer_fn()
print('v1 after outer f_fn',v1)

