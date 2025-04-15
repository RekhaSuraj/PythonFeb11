# Print even numbers from 0 to 10 in a new list

# even_list = []
# for i in range(11):
# 	if i %2 == 0:
# 		even_list.append(i)

# print(even_list)

# [0, 2, 4, 6, 8, 10]

# List comprehension
even_list = [n for n in range(11) if n%2 == 0]
print(even_list)
# [0, 2, 4, 6, 8, 10]

# odd numbers from 0 to 10 hw