# ACCESSING THE ITEMS FROM DICTIONARY - Indexing not allowed

d = {
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
# We can access the using the keys of dictionary.
# 1. Square bracket method []
d1 = {'name': 'tanya', 'age': 21, 'gender': 'female'}
print(d1['name'])
print(d['subjects']['dsa'])    # 2D Dictionary

# 2. Get function -
print(d1.get('age'))
print(d.get('subjects').get('nlp'))      # 2D Dictionary


# ADDING NEW KEY VALUE PAIRS (OR ADDING ELEMENTS)
d1['college'] = 'LPU'
d1['subjects'] = {}
d1['subjects']['ML'] = 95   # for adding a dictionary inside dictionary we first have to create a dictionary empty then add the elements.
print(d1)


# REMOVE ELEMENTS (KEY-VALUE PAIR) FROM DICTIONARY
# Pop - removes the particular key-pair
d2 = {'name': 'tanya', 'age': 21, 'gender': 'female',1:2,3:4,5:6}

d2.pop('age')
print(d2)     # removes 'age' :21

# Popitem - deletes the last item from the dictionary
d2.popitem()
print(d2)     # deletes 5:6

# Del - removes a particular key value pair
del d2[1]
del d['subjects']['dsa']
print(d2)
print(d)

# Clear - deletes all the key-value pair and makes the dictionary empty
d2.clear()
print(d2)


# EDITING EXISTING KEY-VALUE PAIR
d1['name'] = 'Tanya Tarun'
print(d1)

d['subjects']['nlp'] = 65    # For 2D
print(d)


# DICTIONARY OPERATIONS -
# 1. MEMBERSHIP - works on keys not values
print('name' in d1)       # true cz name key is there in d1
print('hello' in d1)      # false cz hello key is not there in d2

# 2. ITERATION - Iterating in dictionary means iterating through the keys not value
for i in d1:
    print(i)   # print all the keys in d1

for i in d1:
    print(i, d1[i])    # i prints the keys and d1[i] prints their expected value
