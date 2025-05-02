f2 = open("demo.txt",'w')
print(f2)
# <_io.TextIOWrapper name='demo.txt' mode='w' encoding='cp1252'>

f2.write("Good Morning Students")
# f2.close()

# f2.write("GM Again")
# ValueError: I/O operation on closed file.

# Print the parameters
print('Is file closed:',f2.closed)
print('File Mode:',f2.mode)
print('FileName:',f2.name)

# Is file closed: False
# File Mode: w
# FileName: demo.txt

f2.close()
print('Is file closed now:',f2.closed)
# Is file closed now: True
