# Common functions - Applicable on all datatypes.

a = 'Tanya Tarun'
print(len(a))  #Counts space too.
print(max(a))  # prints maximum character based on ASCII values
print(min(a))  # prints minimum character based on ASCII values. prints nothing as space as the lowest ascii value.
print(sorted(a)) # Sorts the string but gives the result in a list.


# Functions applicable only on strings
b = 'kunal singh'
print(b.capitalize())   #capitalizes the first letter of string.
print(b.title())      #capitalizes the first letter of every word in the string.
print(b.upper())      # converts every letter of string to uppercase
print(b.lower())      # converts every letter of string to lowercase
print('TaNya'.swapcase())   # converts capital letter to lower and lower to capital
print(a.count('a'))     #gives the count of particular letter from the string.
print(a.find('Tarun'))  #Gives the index of particular substring. Gives -1 if the substring doesnot exists.
print(a.index('Tarun'))    # same as find function but throws error if the string doesnot exists unlike find.
print(a.endswith("n"))
print(a.startswith('ta'))

name = 'Kunal'
gender = 'Kutta'
print('Hi! My name is {} and I am {}.'.format(name, gender))
#This function basically inserts value in the sentence.

print('Tanya1'.isalnum())    #check if string contain alphabet as well as number only.
print('Tanya'.isalpha())    #check if string contain alphabet only.
print('123'.isdigit())    #check if string contain number only.
print('name'.isidentifier())       #check if string contain identifier only.


print('Hi! My name is Tanya'.split())
#stores each word in the list separately like 'hi!', 'My', etc..
print('Hi! My name is Tanya'.split('a'))
#Splits each word where a is there like 'Hi!', 'My', 'n', 'me is T', 'ny', ''.

print('/'.join(['19', '02', '2005']))
#adds / between every words basically joins two words.

print('Tanya Tarun'.replace('Tarun', 'Singh'))
#replaces a particular word with another

print('Tanya Tarun'.strip()) # removes trailing(beginning or ending) spaces not from between two strings.