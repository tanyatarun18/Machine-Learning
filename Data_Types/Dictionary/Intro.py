# Dictionary in python is a collection of keys values, used to store data values like a map, which,
# unlike other data types which hold only a single value as an element.
# In some languages it is known as map or associative arrays.
# dict = {'name': 'tanya', 'age': 21, 'gender': 'female'}

# CHARACTERISTICS -
# Unordered
# Mutable
# Indexing does not work
# Keys can't be duplicated
# Keys can't be mutable items

# CREATING A DICTIONARY
# Empty dictionary
dict1 = {}
print(dict)

# 1D homogeneous dictionary
d = {'name': 'tanya', 'gender': 'female'}
print(d)

# 1D Heterogeneous dictionary
d1 = {'name': 'tanya', 'age': 21, 'gender': 'female'}
print(d1)

# 2D dictionary
d2 = {
    'name': 'tanya',
    'age': 21,
    'college':'lpu',
    'sem' : 4,
    'subjects' : {
        'dsa':50,
        'nlp':62,
        'cv':34
    }
}
print(d2)

# Using type conversion
d3 = dict([('name', 'tanya'), ('age', 21), ('gender', 'female')])
print(d3)
print(type(d3))  # dictionary

# Duplicate keys - Not possible
d4 = {'name':'Tanya', 'name': 'Tanya Tarun'}
print(d4)      # will not print duplicate values. Only the one with update get printed means the last one "Tanya Tarun".

# Mutable items as keys - Not possible
# d5 = {'name':'Tanya', 'age': 21,[1,2,3] : 1}
# print(d5)   # throws  error cz we are using a list which is mutable.
d6 = {'name':'Tanya', 'age': 21,(1,2,3) : 1}
print(d6)   # will not throw any error now cz we have used tuple and that is immutable.
