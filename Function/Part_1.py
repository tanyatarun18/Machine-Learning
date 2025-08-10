# ARGS KEYWORD - THIS IS USED TO ASSIGN ANY NUMBER OF NON-KEYWORD INPUT IN A FUNCTION.
                # IF THE USER IS NOT SURE ABOUT THE NUMBER OF INPUT TO GIVE AS PARAMETER THEN THIS FUNCTION IS USED SO WHILE CALLING THE FUNCTION
                # ANY NUMBER OF INPUT CAN BE THERE AS ARGUMENT AND THE CODE RUNS PERFECTLY FOR ALL.

def find_sum(*args) :
    '''This function is used to find the sum of a list of numbers.
    Also, this is using the args keyword.'''
    sums = 0
    for i in args :
        sums += i

    return sums

print(find_sum(1,2,3,4,5,6,7,8,9,10))

# The above function works and gives the sum 55. So what happens is the argument given while calling gets stored as tuple in the memory and then the loop
# easily iterates through it and performs the operation.
# Also, it is not mandatory to use this with the word 'args' only. We can use any word just with the '*'.


# ACCESSING THE DOCUMENT STRING - DOCUMENT STRING IS BASICALLY WHILE WRITING THE FUNCTION, WE PROVIDE A DOCUMENT UNDER COMMENTS OF WHAT THIS FUNCTION IS USED FOR.
# We can also see the documentation of built-in functions like print.
print(find_sum.__doc__)
print(print.__doc__)


# KWARGS = THIS IS USED TO ASSIGN ANY NUMBER OF KEYWORD ARGUMENT/INPUT IN A FUNCTION.
# KEYWORD ARGUMENTS MEAN THAT THEY CONTAIN A KEY-VALUE PAIR LIKE THE PYTHON DICTIONARY.

def show_items(**list):
    for (key, value) in list.items() :
        print(key, ' - ', value)

show_items(a = 'Chocolate', b = 'Cake', c = 'Noodles', d = 'Cold Drink')
# Same as the args keyword, we can use any name just with '**' to mean it kwargs.

# POINTS TO REMEMBER
# ORDER OF ARGUMENT MATTERS (NORMAL -> ARGS -> KWARGS)
# ANY NAME CAN BE USED. ITS NOT MANDATORY TO USE ARGS AND KWARGS AS NAME. WHAT MATTERS IS '*' AND '**'.

# WHAT HAPPENS IF THERE IS NO RETURN STATEMENT?
# SO BASICALLY IF WE HAVE PUT A RETURN STATEMENT INSIDE THE FUNCTION, SO WHILE CALLING THE FUNCTION WE HAVE PUT THE CALL INSIDE THE PRINT STATEMENT FOR THE OUTPUT
# TO GET PRINTED LIKE IN 'FIND_SUM' FUNCITON.
# AND IF WE USE PRINT INSIDE THE FUNCTION SO WHILE CALLING WE DO NOT USE PRINT STATEMENT LIKE IN 'SHOW_ITEMS' FUNCTION.
# BUT WHAT IF WE USE PRINT INSIDE THE FUNCTION AND WHILE CALLING ALSO (MEANS NO RETURN STATEMENT) SO WHAT HAPPENS IS, THE RETURN GET EXECUTED DEFAULTLY AND PRINTS 'NONE'.

# AN EXAMPLE -
list = [1,2,3,4]
print(list.append(5))    # This will not print the new list but instead print 'None' bcz we are not the print statement to print the list but we are asking to print a change in list.


# VARIABLE SCOPE -
# 1. GLOBAL VARIABLE - GLOBAL VARIABLE ARE THOSE WHICH CAN BE ACCESSED BY THE PROGRAM (ALSO ANY FUNCTION INSIDE THE PROGRAM).
# 2. LOCAL VARIABLE - LOCAL VARIABLE ARE THOSE WHICH CAN BE ACCESSED ONLY BY FUNCTION INSIDE WHICH IT IS CREATED.

def hello(x):
    print(x)
    x = y+x
    print(x)

y = 3
hello(y)


# NESTED FUNCTION - FUNCTION INSIDE FUNCTION.
# THE FUNCTION WHICH IS INSIDE ANOTHER FUNCTION CAN BE DIRECTLY CALLED OUT THE OUTSIDE FUNCTION. TO CALL THE INSIDE FUNCTION, WE HAVE TO CALL THE OUTSIDE FUNCITON.
def func1():
    def func2():
        print("Hello, I am inside function")
    func2()
    print("Hello, I am outside function.")

func1()
#func2()    # will be give error bcz its nested inside a function.