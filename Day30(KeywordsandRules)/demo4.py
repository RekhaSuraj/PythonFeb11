# string program - Write a program to give the count of words in a sentence(string)

str1 = 'Python is fun and easy'
list1 = str1.split()
print(list1)
# ['Python', 'is', 'fun', 'and', 'easy']
count_words = len(list1)
print(count_words)

cnt = 0
for i in str1:
	# print(i)
	cnt = cnt+ 1

print(cnt)


# reverse words in a sentence - hw