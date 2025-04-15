# title - First letter will be updated to capital
str1 = 'welcome to python'
print(str1.title())
# Welcome To Python

# index(): If the substring is found, it returns the index of the first occurrence.
# If the substring is not found, it raises a ValueError exception.
print('------index------')
str2 = 'Hello World'
print(str2.index('l'))
# 2


find_res = str1.find('x')
print(find_res)
# -1

index_res = str1.index('x')
# ValueError: substring not found







