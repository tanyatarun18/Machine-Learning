#reverse a String using a loop
#This is slicing method

a = "Hello"

def reversed_string(a):
    return a[::-1]

print (reversed_string(a))

#Using reversed() and join() function
def reversed_string1(a):
    return "".join(reversed(a))

print (reversed_string(a))

#Using loops
def reverse_string2(a):
    reversed_a = ""
    for char in a:
        reversed_a = char + reversed_a
    return reversed_a

print(reverse_string2(a))
