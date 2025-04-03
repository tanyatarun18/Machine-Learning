# Find the frequency of a character in the particular string

s = input("Enter your string: ")
c = input("Enter the character to be found: ")
cnt = 0

for i in s:
    if(i == c):
        cnt+=1

print("The number of ", c, " in the string is: ", cnt)