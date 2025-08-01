# Frozen set is a immutable version of set.
# The difference b/w these two are same as the difference b/w lists and tuple.

# CREATION OF FROZEN SETS
f1 = frozenset({1,2,3,4,5})
print(f1)

# All the operations like union/ intersection/ difference/ symmetric_difference , etc which worked with sets will work with frozen sets as well because we are not
# making changes in the set we are just reading the values in different manners with these operations.
# Only add and delete will not work because these are making changes in the set.

# WHEN TO USE FROZEN SETS - Whenever we want to make read-only set then we can use this. not with write sets.

# 2D FROZEN SETS - POSSIBLE BECAUSE FROZEN SETS ARE IMMUTABLE AND WE CAN PUT IMMUTABLE ITEMS INSIDE THE SET.
f2 = frozenset({4,5,6, frozenset([7,8])})
print(f2)
