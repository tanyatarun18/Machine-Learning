# BENEFITS OF USING FUNCTIONS -
# 1. CODE MODULARITY - means codes for different purpose are written in different functions so when there's error, it becomes easy
                     # to debug and solve the error the particular section/function causes.
# 2. CODE READABILITY - since different functions are used for different purpose, it becomes eaasy to work in teams and let individual
                       # a single function.
# 3. CODE REUSABILITY - create a function once and call and use it multiple times.


# LAMBDA FUNCTION - A lambda function is a small anonymous function (means a function with no name).
                  # A lambda function can take any number of arguments, but can only have one expression.
                  # We cannot directly access the function. We have to store it in a variable and then access through that variable.
# Expression -  lambda a,b : a+b
               # lambda is a keyword, (a,b) are parameters, (a+b) is what we want to do with the function (basically the logic).
# Example - Print the square of a number.
a = lambda x : x**2
print(a(3))

b = lambda x,y : x+y
print(lambda x,y : x+y)
print(b(3,4))

# DIFFERENCES BETWEEN LAMBDA AND NORMAL FUNCTION -
# 1. Lambda function does not have a name
# 2. Lambda function has no return value (infact if not assigned a variable, it returns a function itself)
# 3. lLambda is written in 1 line.
# 4. Lambda functions are not reusable.

c = lambda x : 'a' in x
print(c('tanya'))

d = lambda x : 'odd' if x % 2 != 0 else 'even'
print(d(2))


# WHY LAMBDA FUNCTION ?
# They are used with HOF (Higher Order Functions)
# HOF are functions that either returns a function or receives a function as parameter
# Example -
def square(a):
    return a**2

def answer(func, list1):
    output = []
    for x in list1:
        output.append(func(x))
    print(output)

list1 = [1,2,3,4,6]

answer(square, list1)

# So, from the above example, we can see that we have passed a function as a parameter to another function to perform the operation. This is called Higher Order function.
# Now, this answer function calculates the square as square function is passed as input but what if now i want to calculate the cube and so to do that I'll have to make
# another function and then for any other task another function, which makes writing code complex. So, to solve this lambda function is used (see below).

answer(lambda a:a**2, list1)      # converted a whole function to single line to code. This is why and where lambda function is used.

# There are some higher-order functions using which we can write the complex function code in 1 line. These accepts 2 inputs - lambda function and an
# iterable(like list, dictionary, etc).

# 1. MAP() - Built-in higher order function that can even make the code even more short.
# Example - we are taking the same example as above and the output will be same with just 1 line of code.

a = list(map(lambda x: x**2, [1,2,3,4,5,6]))
print(a)
# This gives the same output as above. Also, map function gives a memory location as output. We have to convert to list to see the output.

b = list(map(lambda x: 'even' if x%2==0 else 'odd', [1,2,3,4,5,6]))
print(b)       # output = ['odd', 'even', 'odd', 'even', 'odd', 'even']


# 2. FILTER() - This is a built- in higher-order function which filters out based on a condition given.
# Example -
c = list(filter(lambda x:x%2==0, [1,2,3,4,5,6]))
print(c)         # Prints [2,4,6]


# 3. REDUCE() - This is a higher order function inside a module(functools) which performs the operation and return the singe value.
# Example - Sum of all elements of list
import functools
d = functools.reduce(lambda x,y:x+y, [1,2,3,4,5,6])
print(d)      # Prints 21. Here it works with 2 element at a time as we have given input as x and y.
# Also, filter does not require to be converted to list to get the output.

#Difference b/w map and filter is map takes a list and creates a new list of the same size, with each item transformed. Reduce takes a list and boils it down to a
#single value.