print({i:i*3 for i in range(1,11)})

# dictionary using existing dictionary
# Example - to convert km to miles
distance = {'delhi': 1000, 'mumbai': 7000}
print({i:j*0.56 for (i, j) in distance.items()})

# dictionary comprehension using zip() - basically creating a dictionary from other data types.
# Like here we are creating dictionary using 2 lists
reg_no = [1,2,3,4,5,6]
name = ['a','b','c','d','e','f']

print({i:j for (i, j) in zip(reg_no, name)})

# Using if condition -
clss = {1:0,2:5,3:0,4:9,5:6}     # class: number of students
print({i:j for (i, j) in clss.items() if j!=0})
# WE HAVE TO MANDATORILY PUT .ITEMS() BCZ THIS IS GET ALL THE ITEM FOR ITERATION. OTHERWISE DICTIONARY CANNOT BE ITERATED DIRECTLY


# NESTED COMPREHENSION
# Ex - print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range (2,5)})
