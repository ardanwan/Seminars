"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
"""

Function:

function_2c -- Requires four input variables (w,x,y and z)

Arguments:

multiplication = multiplies x and y
division = divides x by y
addition = adds w and z
subtraction = subtracts z from w

results = library with the keys (multiply, divide, add and subtract) -- represents the arguments from the function

Returns:

results

"""
def function_2c(w, x, y, z):

    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
