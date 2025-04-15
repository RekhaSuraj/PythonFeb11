new_list = []
for i in range(5):
	if i%2 == 0:
		new_list.append(i)
	else:
		new_list.append(i+1)

print(new_list)

# List comprehension 
n_list = [k if k%2 == 0 else k+1 for k in range(5)]
print(n_list)

# [0, 2, 2, 4, 4]

