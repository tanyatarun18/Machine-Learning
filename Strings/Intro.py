# In python strings are a sequence of Unicode Characters.

# CREATING A STRING

a = "Tanya"
b = 'Tarun'
c = '''My name is tanya tarun.
I am good in python.'''            # For multiline strings
print(a)
print(c)


# ACCESSING A SUBSTRING FROM A STRING
# INDEXING -
#Positive Indexing - When a string is created, automatically index starting from 0 is assigned to the letters of the string.

print(a[0])    # Prints T

#Negative Indexing - Here, index starting from -1 ,-2, etc is assigned to letters from the last.
print(a[-1])   # Prints a


# SLICING - Here we can extract more than 1 letter at a time.
print(a[0:3])   # Prints Tan
print(a[0:])    #tanya
print(a[0:6:2])  #Tna   here step size is used.
print(a[6:0:-1])  # Reverse print


# EDITING OR DELETING A STRING
# Python Stings are immutable. It cannot be changed once created.

n = "Tanya Tarun"
del n
print(n)

#Deleting a part of string of is not possible because it would create changes and strings are immutable.