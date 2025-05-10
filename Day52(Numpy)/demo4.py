import numpy as np

# Addition of matrix
n = np.array([[1,2,3],[4,5,6]])
n1 = np.array([[7,8,9],[10,11,12]])
n2 = np.array([[0,0,0],[0,0,0]])
print(n)
print(n1)
print()
print(len(n))
for i in range(len(n)): #rows
    print(len(n[i])) #columns
    for j in range(len(n[i])):
        n2[i][j] = n[i][j] + n1[i][j]

print(n2)
print()

n4 = n+n1
print(n4)

# hw - Multiplication of matrix