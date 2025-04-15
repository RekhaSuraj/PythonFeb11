# Convert every letter in a string to uppercase
list1 = ['vittal','aparna','uday','srinivas']

def func_upper(let):
	return let.upper()


# upper_list = tuple(map(func_upper,list1))
# print(upper_list)
# # ('VITTAL', 'APARNA', 'UDAY', 'SRINIVAS')

# using lambda
print(list(map(lambda a:a.upper(),list1)))
# ['VITTAL', 'APARNA', 'UDAY', 'SRINIVAS']

