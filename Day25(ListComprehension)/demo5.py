# print squares of numbers from 1 to 5 into a new list

# sq_list = []
# for i in range(1,6):
# 	sq_list.append(i**2)

# print(sq_list)

# List comprehension
sq_list = [s**2 for s in range(1,6)]
print(sq_list)
# [1, 4, 9, 16, 25]


# Print a new list by adding 2 to every number in the below list
l1 = [20,30,40,50]
new_list = [j+2 for j in l1]
print(new_list)
# [22, 32, 42, 52]
