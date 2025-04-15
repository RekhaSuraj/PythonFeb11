# Write a program to check if a given string is a palindrome

str1 = input('Please enter a string')
if str1 == str1[::-1]:
    print(str1, 'is a palindrome')
else:
    print(str1,'not a palindrome')

# Please enter a stringmom
# mom is a palindrome

# Please enter a stringmad
# mad not a palindrome

# Please enter a stringmadam
# madam is a palindrome