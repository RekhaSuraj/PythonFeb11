# Print only capital letter animals into a new list
l2 = ['Cat','DOG','COW','Goat','SHEEP']

cap_list = []
for i in l2:
	if i.isupper():
		cap_list.append(i)

print(cap_list)

# ['DOG', 'COW', 'SHEEP']

# List Comprehension
c_list = [c for c in l2 if c.isupper()]
print(c_list)
# ['DOG', 'COW', 'SHEEP']