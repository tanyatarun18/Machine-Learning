# LEN/SORTED/MIN/MAX
d1 = {'name': 'tanya', 'age': 21, 'gender': 'female'}

# LEN - GIVES THE SIZE OF DICTIONARY
print(len(d1))

# SORTED - SORTS THE DICTIONARY IN ORDER OF THEIR KEYS
print(sorted(d1))        # sorts in ascending order
print(sorted(d1, reverse = True))       # sorts in descending order

# MIN/MAX - GIVES THE MINIMUM AND MAXIMUM KEY BASED ON ASCII VALUE
print(min(d1))
print(max(d1))

# ITEMS/KEYS/VALUES
print(d1.items())      # Print all the key-value pairs in the form of tuples
print(d1.keys())       # Prints all the keys
print(d1.values())     # Prints all the values

# UPDATE - USING THIS FUNCTION WE CAN UPDATE A GIVEN DICTIONARY WITH ANOTHER DICTIONARY
d2 = {1:2, 3:4, 4:5}
d3 = {4:8, 5:6}
d2.update(d3)
print(d2)
