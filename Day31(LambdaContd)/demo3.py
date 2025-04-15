# sorting based on 0th index by dafault using sort()

s1 = [(2,-4,6),(1,3,7),(3,8,-2),(5,-3,9)]

s1.sort()
print(s1)

# sorting based on 1st index using sorted(iterable,key=fun_name)
def fetch_second_index(s1):
	return s1[1]

# print(help(sorted))
# sorted()

new_list = sorted(s1,key=fetch_second_index)
print(new_list)
# [(2, -4, 6), (5, -3, 9), (1, 3, 7), (3, 8, -2)]

# using lambda
n_list = sorted(s1,key=lambda x:x[1])
print('lambda',n_list)
# lambda [(2, -4, 6), (5, -3, 9), (1, 3, 7), (3, 8, -2)]

