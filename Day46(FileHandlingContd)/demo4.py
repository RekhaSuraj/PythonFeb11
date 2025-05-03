# readlines :The readlines() method returns a list of lines from the file.

# with open('demo.txt','r') as file:
#     print(file.readlines())

# ['Good Morning Students\n', 'Welcome to Python class\n', 'Welcome to SQL class\n', 'Welcome to Django class']

with open('demo.txt','r')as file:
    file.seek(10) # moves the cursor to byte 10
    print('cursor point',file.tell()) #should print 10
    print(file.read(10)) #print - read 10 char(bytes) - will print 'ng Student'
    print(file.tell()) # should print 20

#How it works

# file.seek(10) moves the file cursor to the 10th byte.
# file.tell() returns the current cursor position.
# file.read(10) reads 10 characters from that position.
# The second file.tell() shows the new position after reading.

