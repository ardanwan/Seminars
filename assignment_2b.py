"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""

""" 
Function:

function_2b = requires two strings as input

Argument:

lower = makes the first string into lowercase
upper = makes the second string into lowercase
combined = adds the two strings together

dict = Library with keys L, U and C which stand for the arguments of this function

Returns:

dict

"""

def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
