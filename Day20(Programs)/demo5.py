str1 = "Today is a good Day"

# Replace 'o' with '&' in the above list without using inbuilt method
str2 = str1.replace('o','&')
print(str2)
# T&day is a g&&d Day

res = ''
for i in str1:
	if i == 'o':
		res = res + '&'
	else:
		res = res + i


print('result string:',res)
# result string: T&day is a g&&d Day



