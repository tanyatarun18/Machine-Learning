# ACCESSING ITEMS FROM A TUPLE
# Indexing -

t = (1,2,3,4,5,6)
t1 = (1,2,3,4,5,6)
print(t[1])
print(t[-2])

# Slicing -
print(t[-3:])
print(t[:4])
print(t[::2])

# Same as list we can access elements.

# EDITING A TUPLE - We cannot edit or change elements in tuple as these are immutable.
# ADDING ITEMS - We cannot add items in existing tuple as adding would make changes in tuple which is not allowed as tuples are immutable.
# DELETING ITEMS - We cannot also delete the items as it would make changes in tuple
                   # but we can delete the whole tuple.
del t1
#print(t1)

# OPERATORS IN TUPLES
# Arithmetic Operations - '+' , '*'
t2 = (1,2,3,4,5,6)
print(t+t2)     #Concatenates the tuples

print(t * 2)   #Multiplies and print the tuple

# Membership Operator - 'in' , 'not in'
print(1 in t2)          # Print true as 1 in there in tuple t2
print(1 not in t2)      # Print false as 1 is there.

# Iteration - Means using loops as same in list.
for i in t2:
    print(i)


#Swaping without using third variable is possible in python.
a = 1
b = 2
a,b = b,a
print(a,b)
