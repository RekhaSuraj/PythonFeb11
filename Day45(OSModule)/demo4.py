# File Handling

# What is File?
# Files are named location on disk to store information
# They are used to keep data permanently.
# We  can retrieve data whenever required
#
# Types of File
# Text File: Text file usually we use to store character data. For example, test.txt
# Binary File: The binary files are used to store binary data such as images, video files,
# audio files, etc.
#
# Create File in Python: You'll learn to create a file in the current directory or a specified
# directory.
# Also, create a file with a date and time as its name. Finally, create a file with permissions.
# Create A Empty Text File
# We don’t have to import any module to create a new file. We can create a file using the
# built-in function open().


#     'r'       open for reading (default)
#     'w'       open for writing, truncating(delete) the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)

# syntax : open(filename,mode)

# x : Open a file only for exclusive creation. If the file already exists, this operation fails.

f1 = open("demo.txt",'x')
print(f1)
# <_io.TextIOWrapper name='demo.txt' mode='x' encoding='cp1252'>

# If we try to create it again like below, we get error
# f1 = open("demo.txt",'x')
# FileExistsError: [Errno 17] File exists: 'demo.txt'