"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    # This function takes as input four numbers as ints: w, x, y, z in that order.

    # The numbers x and y are used for multiplication and division where x*y and x/y are calculated
    # The numbers w and z are: 1. added and 2. subtracted with w the first value.
    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    # Again the function return a dictionary which stores the values under the keys multiply, divide, add and subtract
    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
