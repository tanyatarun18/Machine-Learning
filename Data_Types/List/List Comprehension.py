# LIST COMPREHENSION = List comprehension provides a concise way of creating lists.
# newlist = [expression for item in iterable if condition==True]
''' Advantages :
1. More Time-Efficient and space efficient and space-efficient than loops.
2. Require fewer lines of code.
3. Transforms iterative statement into a formula.
'''
# EXAMPLES -
# 1. Add 1 to 10 numbers to a list

# Manual
l = []
for i in range(1,11):
    l.append(i)
print(l)

# List Comprehension
l = [i for i in range(1,11)]
print(l)

# 2. Scalar multiplication on a vector
l1 = [1,2,3]
l2 = 3
#Manual
l3 = []
for i in l1:
    l3.append(i*l2)
print(l3)

# List comprehension
print([l2*i for i in l1])

# 3. Add Squares
#list comprehension
print([i*i for i in l1])

# 4. Print all the numbers divisible by 5 in the range of 1 to 50
print([i for i in range(1, 51) if i%5==0])

#Find languages which start with letter p
languages = ['java', 'php', 'python', 'ruby', 'c++', 'javascript']
print([i for i in languages if i.startswith('p')])

# Nested if with list comprehension example
basket = ['apple', 'orange', 'avocado', 'banana']
fruits = ['apple', 'kiwi', 'banana', 'avocado']

print([i for i in fruits if i in basket if i.startswith('a')])

#Print a (3,3) matrix using list comprehension
print([[i*j for i in range(1,4)] for j in range(1,4)])

#Cartesian product
a = [1,2,3,4]
b = [4,5,6,7]

print([i*j for i in a for j in b])
