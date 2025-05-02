# append in the file
f1 = open('demo.txt','a')
content1 = f1.write('\nWelcome to Python class')
content2 = f1.write('\nWelcome to SQL class')
content3 = f1.write('\nWelcome to Django class')
# To print number of characters(int)
print(content1,content2,content3)

f1.close()

# Good Morning Students
# Welcome to Python class
# Welcome to SQL class
# Welcome to Django class