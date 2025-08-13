# FUNCTIONS ARE FIRST-CLASS CITIZENS - In programming language, a first-class citizen is an entity which supports all the operations generally available to other entities.
                                      # These operations typically include being passed as an argument, returned from a function, and assigned to a variable.
                                      # Generally, in other languages, data types are first-class citizen but in python along with data types, functions are also
                                      # first-class citizens.
                                      # Functions are immutable.

# Similar to data types, we can perform operation on functions like -
# 1. TYPE AND ID -
def product(num):
    return num*num

print(type(product))     # Prints function
print(id(product))

# 2. REASSIGN -
a = product     #This will work perfectly although product is a function
print(a(3))     # Prints 9
print(id(a))     # Same as id of product

# 3. DELETING A FUNCTION -
'''del product
print(product)'''      # gives error bcz function now does not exist.

# 4. STORING -
list = [1,2,3,4,5,product]
print(list)      # Prints <function product at 0x00000276892E32E0> for product

# 5. RETURNING A FUNCTION FROM A FUNCTION-
def func():
    def x(a,b):
        return a+b
    return x

y = func()(1,2)
print(y)
# So, what happens here is, the func() in y is calling the function func() then inside the func, it goes to function x which returns x so now in y, the func() gets
# changed to x and then x(1,2) is actually happening in y and this gets printed 1+2 = 3.

# 6. FUNCTION AS ARGUMENT -
def a():
    print("Inside function a")

def b(x):
    print("Inside function b")
    return x()

print(b(a))
# Here, we get to program and see function a and then b and then jump to print statement of function call. There it call function b.
# We go to b where we have parameter x which will be replaced by function a bcz in argument of b we gave function a. the 'inisde function b" gets printed now.
# Then b return x as function which means return function a so the compiler go to a and prints "inside function a".
# And then none gets printed bcz no return statement is there in a.