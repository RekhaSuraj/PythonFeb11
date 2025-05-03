# Read Binary files  by using the ' rb ' :
# In Python, 'rb' in open('emp1.jpeg', 'rb') stands for:
#
# r = read mode (you want to read the file)
# b = binary mode (you want to read the file as binary data, not as text)
# When dealing with non-text files like images, PDFs, audio, video, etc., you should use binary mode so Python doesn't try to decode the file as text (which could corrupt the data).

with open('emp.jpg','rb')as pic:
    print(pic.read())

n1 = open('emp.jpg','rb')

n2 = open('pic.jpg','wb')
for i in n1:
    n2.write(i)

print(n2)
