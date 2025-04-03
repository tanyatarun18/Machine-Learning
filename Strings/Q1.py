# Find the length of a string without using len() function.

s = input("Enter your string: ")
len = 0

for i in s:
    len+= 1

print("Length of the string is: ", len)