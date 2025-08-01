'''Find the Maximum Character (by ASCII) in a String
Problem:
Write a function that returns the character with the highest ASCII value in a given string.
Example:

Input: "kunal singh"
Output: 'u' '''

a = input("Enter a string: ")

dict = {}
for i in a:
    dict[i] = ord(i)
print(dict)

initial_val = 0
for value in dict.values():
    if value > initial_val:
        initial_val = value

for key, value in dict.items():
    if(value == initial_val):
        print("The character with the highest ASCII value is: ", key)
        break