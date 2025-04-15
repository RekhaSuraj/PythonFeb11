def first_sum(n1,n2,n3):
	sum1 = n1+n2+n3 #30

	def second_sum(s1,s2,s3):
		sum2 = s1+s2+s3 #60

		return sum2

	s2 = second_sum(10,20,30) #60
	# print(s2)
	return s2+sum1


total = first_sum(5,10,15)
print(total)
# 90

# Function returns Even or Odd
def even_odd(num):
    if num%2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(even_odd(6))
var1 = even_odd(7)
print(var1)

# hw using functions
# largest number among 3 inputs from user
# Smallest number in a list
# Length of a list without using len()

# Print prime numbers from 2 to 20 without function first
# Next try with function

list1 = [10,5,90,20,30]

def big_number(list1):
	big = list1[0]
	for i in list1:
		if i > big:
			big = i

	return big


n1 = big_number(list1)
print(n1)





