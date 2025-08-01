# Two operators work with lists.
# ARITHMETIC - only '+', '*'
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1 + list2)    # Merges both the lists in 1 list
print(list1 * 2)       # prints the values of lists the number of times the no the number it is multiplied with.

# MEMBERSHIP OPERATOR - finds if 1 thing is there in the other.
print(5 in list1)      # prints true because 5 is there in list1
print(7 not in list2)   #prints false because 7 is there in list2


# LOOPS
for i in list1:
    print(i)    #prints all the elements of the list.
list3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
for i in list3:
    print(i)   # Loop will run 2 times kyuki bahar wale list me 2 hi items h.

