# control flow statements
# In Python, 1. continue, 2. break, and 3. pass are control flow statements used in loops and conditional statements, but they behave differently:
#
# 1. break
# Exits the loop completely. - Looping statements

for i in range(10):
    if i == 3:
        break # it will exit the for loop immediately
    print(i)

# 0
# 1
# 2

print('----------')
# 2. continue - Skips the current iteration and moves to the next iteration of the loop.

for i in range(10):
    if i == 3:
        continue # 3rd iteration is skipped here
    print(i)

# 0
# 1
# 2
# 4
# 5
# 6
# 7
# 8
# 9

# 3. pass
# Does nothing; it is a placeholder where a statement is syntactically required but not implemented yet.
for i in range(10):
    pass


def function_name():
    pass


class Test:
    ...


# Statement	Function
# break		Exits the loop entirely
# continue	Skips the current iteration and continues to the next
# pass		Does nothing, acts as a placeholder