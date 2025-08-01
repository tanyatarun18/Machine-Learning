# ACCESSING ITEMS FROM THE LIST
# 1. Indexing - Accessing single element at a time

list = [1,2,3,4,5]
list1 = [1,2,3,[4,5],6]
list2 = [[[1,2],[3,4]],[5,6]]

# Positive Indexing : Indexing start from 0 and from left to right
print(list[1])  #prints 2
print(list1[3][1])     #prints 5

# Negative indexing : Indexing start from -1 and from right to left
print(list[-1])   #prints 5
print(list1[-2])  #prints [4,5]
print(list1[-2][-1])    #prints 5
# So, to access elements from 2D list, we need to use 2 [], for 3D list, 3 [].

print(list2[0][0][1])    #prints 2,   3D list


# 2. Slicing -  Accessing single/multiple elements at a time(Same as string)
print(list[0:3]) #print [1,2,3]
print(list[-3:])  #prints [3,4,5]


#ADDING ITEMS TO A LIST
# Append - Adding single items to the end of the list
list.append(6)
list.append([4,2,5])   #prints [1, 2, 3, 4, 5, 6, [4, 2, 5]]
# although append add a single item only but these elements will still be added but as a single item.
print(list)

# Extend - Adding multiple items at the end of list
list.extend([7,8,9])
list.extend('tanya')  #prints 1, 2, 3, 4, 5, 6, [4, 2, 5], 7, 8, 9, 't', 'a', 'n', 'y', 'a']
# although extend add multiple items but will still add this single item but by splitting each character of it and storing it as multiple items.
print(list)

# Insert - Adding elements at a desired position, 1 element at a time
list1. insert(3,5)  #first the position and then the element to be addedd
print(list1)


# EDITING EXISTING ITEMS IN A LIST
list3 = ['a','b','c','d','e']
print(list3)

# Editing through indexing
list3[0] = 't'
list3[-4] = 'a'

# Editing through slicing
list3[2:4] = ['n','y']
list3[-1:] = ['a']

print(list3)

list4 = ['10', '9', '8', '7', '6']
#DELETING AN ITEM IN THE LIST
# DEL - Deleting a list through indexes
# Deleting an item in the list through indexing
del list3[0]
print(list3)

# Deleting an item in the list through slicing
del list[0:3]
print(list)

#Deleting the whole list
del list1
#print(list1)

# REMOVE - Deleting a list through values rather than indexes
list4.remove('10')
print(list4)

# POP - Deleting an item through index or defaultly deleting last element.
list4.pop(1)
print(list4)

list4.pop()    #no index given so by default deletes last elements
print(list4)


# CLEAR  - Deletes all elemnts of the list but the empty list exists.
list4.clear()
print(list4)