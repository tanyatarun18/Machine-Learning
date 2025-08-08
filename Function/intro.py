# FUNCTIONS ARE THE BLOCK OF CODE WHICH WHEN GIVEN SOME INPUT, GIVES AN OUTPUT.
# THE MAIN PURPOSE/USE OF THE FUNCTION IS CODE REUSABILITY.
# FUNCTION USES 2 PRINCIPLES -
# 1. ABSTRACTION- This means something is there but not visible and we don't even care. Like there is some code inside the function but not visible
                # and we just care about what input to give.
# 2. DECOMPOSITION - This means something is build up from small parts. For ex - to make a website, we can use different functions (small parts) for
                     # different purpose inside the website and call them together to complete the full-fledge website.
# COMPONENTS OF FUNCTION -
# 'def' keyword 'name' (input) :
#  doc (a user manual - something commented out to just understand the use of function for everyone) - not required but recommended.
#      logic (body)
#      return statement
# name (input) - calling the function


# CREATING A FUNCTION
def is_even(n) :
    '''This functions returns if a given number is odd or even
    input - any valid integer
    output - odd or even'''
    if(n%2==0):
        return 'even'
    else:
        return 'odd'

print(is_even(5))  # calling the function

# PARAMETER vs ARGUMENT
# When the function is created, the input given is parameter.
# When calling/using the function, the input/value given is argument.


# TYPES OF ARGUMENT -
# 1. DEFAULT ARGUMENT - Suppose we have given 2 parameters and while using the function, the user gives only 1 / no arguments so in that case the code will give error.
                       # so to avoid that for a user, we can give a default value/ argument to that parameter and that will be default argument.
                       # and then even with 0 argument while calling, the code will give some output.
                       # Ex - def is_even(n = 1) :
                       #        if(n%2==0):
                       #           return 'even'
                       #        else:
                       #           return 'odd'
                       #        print(is_even())

# 2. POSITIONAL ARGUMENT - So this is basically the regular argument we are generally using like we have fun(a,b) and while calling this function we use fun(3,4).
                          # Here the compiler automatically detects that the value 3 is for a and 4 is for b so this is positional argument.

# 3. KEYWORD ARGUMENT - this argument is basically we pass the argument along with the parameter. Ex - We have fun(a,b) and while calling we use func(b=5, a=7).
                       # So here although in place of 'a' we wrote 'b' argument i.e, 5 but still the function will understand the value 5 for b as we have specified the
                       # value with argument.
                       # This argument is very important bcz while writing code we do not always remember at what position we put what parameter. so using this we just
                       # need to remember the parameters and we can specify while calling.
