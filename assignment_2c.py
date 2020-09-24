"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly

The function_2c takes 4 parameters as input
parameters:

input(w, x, y, z)

multiply: x * y
division: x / y
addition: w + z
substraction: w - z

outputs results in form of a dict with entries named after the
"""
def function_2c(w, x, y, z):
    """
    The function_2c takes 4 parameters as input(w, x, y, z). The output is a dictionary.
    This dictionary contains entries: multiply, division, addition, substraction.

    multiply: x * y
    division: x / y
    addition: w + z
    substraction: w - z
    """

    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
