# BUILT-IN FUNCTIONS - LEN / SUM / MAX / MIN / SORTED
s = {1,2,3,4,5,6}
print(len(s))
print(sum(s))
print(max(s))
print(min(s))
print(sorted(s))   # gives the result in list

# UNION / UPDATE
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))  # works same as (|) operator
s1.update(s2)
print(s1)   # Adds the element of s2 into s1 but how the (|) does (means add only the element from s2 which are not there in s1) and there will be no change in s2.
            # Only s1 changes permanently.

# INTERSECTION / INTERSECTION_UPDATE
print(s1.intersection(s2))   # same as (&) operator
s1.intersection_update(s2)   # works same as update but in intersection and everything is same as above.
print(s1)

# DIFFERENCE / DIFFERENCE_UPDATE
s3 = {1,2,3,4,5}
s4 = {4,5,6,7,8}
print(s3.difference(s4))  # works same as (-) operator
s3.difference_update(s4)  # works same as update but in difference and everything is same as above.
print(s3)

# SYMMETRIC_DIFFERENCE / SYMMETRIC_DIFFERENCE_UPDATE
s5 = {1,2,3,4,5}
s6 = {4,5,6,7,8}
print(s5.symmetric_difference(s6))   # works same as (^) operator
s5.symmetric_difference_update(s6)   # works same as update but in symmetric difference and everything is same as above.
print(s5)

# ISDISJOINT - CHECKS IF BOTH THE SETS ARE DISJOINT SETS. DISJOINT SETS ARE THOSE WHICH DOES NOT HAVE ANY ELEMENT IN COMMON.
s7 = {1,2,3,4,5}
s8 = {4,5,6,7,8}
s9 = {11,12,13,14,15}

print(s7.isdisjoint(s8))    # Prints false because elements are there in common
print(s7.isdisjoint(s9))    # prints true because no elements are common.

# ISSUBSET - CHECKS IF A SET COMES UNDER ANOTHER SET
s10 = {1,2,3}
print(s10.issubset(s7))    # Prints true cz the elements of s10 are all there in s7 means it is a subset of s7.

# ISSUPERSET -
print(s7.issuperset(s10))   # Prints true cz s10 contains s7 along with other element means it is a superset of s7.

# COPY - CREATES A SHALLOW COPY OF A SET MEANS ALTHOUGH THE ELEMENTS ARE COPIED AND SAME IT BOTH OF THEM ARE STORED IN DIFFERENT LOCATIONS.
s11 = s10.copy()
print(s11)