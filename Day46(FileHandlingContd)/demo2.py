# Advantage of with keyword ,  there is no need to file close
# using the with file will be close automatically(without manually)

# read() - Read from underlying buffer until we have size characters or we hit EOF. Reads the contents of the file

with open('demo.txt','r') as file:
    print(file.read())

print(help(file.read))
print(file.closed)

