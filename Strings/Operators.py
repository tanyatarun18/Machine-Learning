# ARITHMETIC OPERATIONS
# Only + and * is supported in python strings

print('Tanya' + " " + "Tarun")  # Concatenates the string
print('Tanya '*2)   # Prints the number of string with what we multiply.


# RELATIONAL OPERATIONS
# All operators are supported

print('Tanya' == 'Tarun')
print('Tanya' == 'Tanya')
print('Tanya' == 'tanya') # False because of T and t as it different in ascii values.
print('Tanya' > 'Tarun')
#We compare string on the basis of its ASCII value. It is lexiographically compared.


# LOGICAL OPERATIONS
# empty strings '' are false in python and non empty 'hello' is true.
print('hello' and 'World')
#this prints world because with 'and' we see if both are true. so first hello is evaluated which is true but to analyze whole statement the compiler will check world also which true too so it will print world.

print('hello' or 'World')
#this will print hello because with 'or' we see if any of the string is true. so first hello is evaluated which is true so without going to other string it prints hello as or needs any of the string to be true.

print(not "")
#prints true because empty string is false and not of false is true.


# LOOPS ON STRINGS

for i in 'tanya':
    print(i)
# prints t, a , n , y ,a.

for i in 'tanya':
    print('hello')
#prints hello the number of times the number of letters are there in tanya.


# MEMBERSHIP OPERATION
print('T' in 'Tanya')  #prints true as T is there in Tanya