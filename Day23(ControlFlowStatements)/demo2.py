# In Python, a while loop can have an else clause.
# The else block executes only if the loop completes normally (i.e., without encountering a break)

# while condition:
#     # Loop body
# else:
#     # Executes if the loop runs to completion (condition becomes False)


# Example 1: while with else (Normal Execution)

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed without a break.")

# 1
# 2
# 3
# Loop completed without a break.


