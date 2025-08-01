# Len / min / max / sum / sorted

t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(min(t1))
print(max(t2))
print(len(t1))
print(sum(t1))     # Adds all the number inside the tuple and give the sum
print(sorted(t2))
print(sorted(t2,reverse = True))   # Sorts in descending order.

# Count , Index
print(t1.count(2))  # Gives the occurrence of the particular element. Prints 0 if element does not exist.
print(t1.index(3))   #Gives the index of particular element. Throws error if element does not exist.

# Zip function - basically converts multiple things to a zip and when to see the value we have convert the zip to list or tuple.
a = (1,2,3,4)
b = (5,6,7,8)

print(zip(a,b))
print(list(zip(a,b)))
print(tuple(zip(a,b)))