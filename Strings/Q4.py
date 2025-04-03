# remove a particular character from string.

s = input("Enter your string: ")
c = input("Enter the character to be removed: ")
ans = ''

for i in s:
    if(i != c):
        ans = ans + i

print("The updated string is: ", ans)
