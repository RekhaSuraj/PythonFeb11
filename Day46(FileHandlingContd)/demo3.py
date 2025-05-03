# readline()	The readline() method reads a single line from a file at a time. .
# Accepts optional size parameter that mentions how many bytes to return from the file.

# with open('demo.txt','r') as file:
#     print(file.readline())

# Read a single line
# Good Morning Students

# Reading 2 lines
# with open('demo.txt','r') as file:
#     print(file.readline(),end='')
#     print(file.readline(),end='')

# using for loop with definite number of iterations
# with open('demo.txt','r') as file:
#     for i in range(1,5):
#         print(file.readline(),end='')

# for loop using file as a iterable
with open('demo.txt','r')as file:
    for line in file:
        print(line,end='')
