# Tuples in python are similar to list.
# The major difference b/w the two is that tuples are immutable. We cannot change the elements of a tuple once assigned.

# Characteristics -
# Ordered
# Unchangeable
# Allows duplicate

# CREATING A TUPLE
tuples = ()   #This is an empty tuple
print(tuples)

t1 = (1)
print(type(t1))
# so we cannot make a single element tuple like created above as while checking for type, it shows integer not tuple.
# this is the correct syntax of creating a single element tuple.
t2 = (2,)
print(t2)
print(type(t2))

# Homogeneous tuple
t3 = (1,2,3,4,5)
print(t3)

# Heterogeneous tuple
t4 = (1,2,'a','b',print,True,[1,2,3,4])
print(t4)

# 2D tuple
t5 = (1,2,3,(4,5,6))
print(t5)

# Using type conversion
t6 = tuple('Tanya')  # Converts this string into a tuple and prints ('T', 'a', 'n', 'y', 'a')
print(t6)

# DIFFERENCE BETWEEN LISTS AND TUPLES
# Syntax
# Mutable
# Speed - immutable datatypes are faster
# Memory - tuples takes less memory
# Built-in functions - More in list
# Error prone - list is more error prone
# Usability   