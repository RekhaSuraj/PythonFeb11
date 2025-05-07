# UseCase:
def read_large_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line  # yield each line one at a time


# for line in read_large_file("sample_text.txt"):
#     print(line.strip())  # or process the line

# ob1 = read_large_file("sample_text.txt")
# cnt = len(ob1)

# If we have to restrict to 10 lines
line_cnt = 0
for line in read_large_file("sample_text.txt"):
    print(line.strip())
    line_cnt += 1
    if line_cnt == 10:
        break



