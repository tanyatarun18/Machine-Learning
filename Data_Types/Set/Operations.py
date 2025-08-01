# ACCESSING THE ELEMENTS - NOT POSSIBLE
# INDEXING AND SLICING NOT POSSIBLE (POSITIVE OR NEGATIVE) BECAUSE SETS ARE UNORDERED

# EDITING THE ITEMS - NOT POSSIBLE BECAUSE INDEXING/SLICING IS NOT POSSIBLE

# ADDING THE ITEMS - POSSIBLE
# Add()
s = {1,2,3,4,5}
s.add(6)
print(s)
# Since sets are unordered, the element can be added at any place in the set and 1 element can be added at a time using the add().

# Update()
s.update((9,7,10))
print(s)
# Multiple elements can be added using this function. the elements are passed using a list or a tuple.

# DELETING THE ITEMS - POSSIBLE
# Del - Deletes the whole set
s1 = {1,2,3,4,5}
print(s1)
del s1
#print(s1)

# Discard - Deletes the particular item
s.discard(3)
print(s)
# If we are trying to delete an item not present in the set, it will not delete anything and will also not throw error

# Remove - same as discard but if the item does not exist, it will throw error
s.remove(2)
print(s)

# Pop - Deletes any item randomly
s.pop()
print(s)

# Clear - Deletes everything from the set and gives the empty set
s.clear()
print(s)