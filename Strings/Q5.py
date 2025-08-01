# Write a Python function that takes a string as input and returns the sentence with word order reversed.
'''Example:
Input: "I love Python"
Output: "Python love I" '''

a = input("Enter the string: ")

b = (a.split())
print(b)
print(type(b))
c = (b[::-1])
d = " ".join(c)
print(d)