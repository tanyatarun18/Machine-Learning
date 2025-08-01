# List - A data type used for storing multiple data/items. A list is a dynamic array.

# CREATING A LIST -
#Empty
print([])

# 1D list
print([1,2,3,4,[5,6]])

# 2D list
print([[1,2,3,4],[5,6]])

# 3D list
print([[1,2,3,4],[5,6], [7,8,9]])

#Type Conversion
print(list("Tanya"))

# Array vs List
# list are dynamic while arrays are fixed
#Lists can store data of multiple data type while arrays cannot
# Lists occupy more memory that arrays
# List takes more time to execute than arrays.

# How are lists stored in memory?
# So, the elements of lists are stored at different locations in the memory and the address of those items are stored in contiguous
# locations then. This is also called referential arrays.

# Characteristics of list
# Ordered
# Mutable data type
# Heterogeneous - store multiple datatype
# can have duplicates
# can be nested
# items can be accessed
# can contain any type of object in python -
# example -
l = [1,2,print,type,input]
print(l)   #this list stores any kind of data/object as in this it stores a built in function - print,type and a class - type.
# are dynamic


# Disadvantages of Python lists
# Slow
# Risky usage - because it is mutable
a = [1,2,3]
b = a
print(a)
print(b)
a.append(5)
print(a)
print(b)   # making changes in a also made changes in b because while assigning a to b, both points to same memory location
           # and because of that changes in a also makes changes in b. To not let that happen, we can use copy function.
# Eats up more memory
