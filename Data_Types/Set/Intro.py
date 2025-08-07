# A set is an unordered collection of items. Every set element is unique (no duplicate) and must be immutable.
# This means sets are mutable but cannot contain mutable data type element with it (e.g, set cannot contain list or a set.
# like there cannot be a 2d set bcz 2d set is a set within set and set is mutable).
# Sets can be used to perform mathematical operations like union, intersection, symmetric,difference, etc.
# Characteristics:
# Unordered
# Mutable
# No duplicates
# Can't contain mutable data types

# CREATING SETS
# Empty
s = {}     # this way we create a dictionary not a set cz both share same syntax '{}'.
print(type(s))    # dict

s1 = set()     # this is the correct way to create an empty set.
print(type(s1))     # prints set

# 1D or 2D(2d not possible)
s2 = {1,2,3}     # homogeneous 1D set
s3 = {1,'a',2,'b'}      # heterogeneous 1D set
s4 = {1,'a',2,'b', True}
# will only print 4 elements not True cz duplicates not allowed and python treats true as 1 and 1 is already there.
print(s2)
print(s3)

# using type conversion
s5 = set([1,2,3,4])
print(s5)

# set can't have mutable items
s6 = {1,2,{3,4}}
print(s6)      # gives error