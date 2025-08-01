# len/min/max/sorted
lists = [4,5,3,1,9]
print(len(lists))
print(min(lists))
print(max(lists))
print(sorted(lists))   # By default sorts in ascending order
print(sorted(lists, reverse=True))   #adding this parameter, sorts the list in descending order
#this sorted operation is not permanent, which means the original list will remain the same and a new object will be returned when function is used.
print(lists)  #The original list will be printed as the operation was not permanent.

# Count - Counts the frequency/number of an element
list1 = [4,5,3,5,1,9,1,2,4,5]
print(list1.count(5))     # prints 3

# Index - Gives the index of an element. If an element is multiple times, it gives the index of first occurrence.
print(list1.index(1))

# Reverse - reverses the list permanently, which means it makes changes in the original list.
list1.reverse()
print(list1)

# Sort - Sorts the list permanently. Even if if we try to print the list without using the function, it will print the sorted list.
list1.sort()
print(list1)

# Copy - Creates a shallow copy(means makes the copy of the object but the address is different) of the list in the memory
list2 = list1.copy()
print(list1)
print(id(list1))
print(list2)
print(id(list2))
# both the lists are same but their address is different.


# 2 WAYS TO TRAVERSE A LIST
# ITEMWISE -
l = [1,2,3,4,5]
for i in l:
    print(i)    # prints all the elements inside the list

# INDEXWISE -
for i in range(0, len(l)):
    print(i)       # prints the indexes of the elements
    print(l[i])     # now this prints the elements of the list


# Zip - the zip function returns a zip object (pair), which is an iterator of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
# iterator = list(here)
# example - Write a program to add items of 2 lists indexwise. Basically same index ke element ko add krke list m daalna h.
l1 = [1,2,3,4]
l2 = [5,6,7,8]
print(zip(l1,l2)) # this basically pair uo the element at same indexes. we can see that through conversion to a list.
print(list(zip(l1,l2)))   # so this prits the pairs

print([i+j for i,j in zip(l1,l2)])  # this pairs up the lists and then add the elements indexed i for the first element of pair and j for second element of pair.