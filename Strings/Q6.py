'''Write a function that counts the number of vowels (a, e, i, o, u) in a given string.
Example:

Input: "Tanya Tarun"
Output: 4 '''

a = input("Enter a string: ")
b = ['a','e','i','o','u']
cnt = 0

for i in a:
    for j in b:
        if(i == j):
            cnt+=1
print(cnt)