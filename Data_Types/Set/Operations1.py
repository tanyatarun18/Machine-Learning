s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}

# UNION (|) - PRINTS ALL THE ELEMENTS FROM EACH SET (DOES NOT PRINT THE DUPLICATE ELEMENTS)
print(s1 | s2)

# INTERSECTION (&) - PRINTS THE COMMON ELEMENT FROM BOTH THE SETS
print(s1 & s2)

# DIFFERENCE (-) - PRINTS THE ELEMENT FROM 1 SET WHICH IS NOT PRESENT IS ANOTHER
print(s1 - s2)  # prints the element of s1 which is not present in s2
print(s2 - s1)  # prints the element of s2 which is not present in s1

# SYMMETRIC DIFFERENCE (^) - PRINTS ALL THE ELEMENTS FROM BOTH THE SETS EXCEPT THE COMMON ELEMENT.
print(s1 ^ s2)  # prints everything except 5

# MEMBERSHIP TEST (IN / NOT IN) -
print(1 in s1)    # TRUE
print(9 in s1)    # FALSE

# ITERATION
for x in s1:
    print(x)