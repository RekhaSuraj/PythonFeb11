# Print count of even numbers and odd numbers from  0 to 11

even_list=[]
odd_list = []
even_cntr = 0
odd_cntr = 0
for v in range(20):
	if v % 2 ==0:
		# print(v)
		even_list.append(v)		
		even_cntr += 1 
		# print('even_cntr',even_cntr)

	else:
		odd_list.append(v)	
		# print(v)	
		odd_cntr += 1
		# print('odd_cntr',odd_cntr)

print(even_list,even_cntr)
print(odd_list,odd_cntr)

