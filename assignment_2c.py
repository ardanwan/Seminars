"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Takes in four variables (v1, v2, v3, v4). 
    returns dict with:
        multiply: v2 * v3
        divide: v2 / v3
        add: v1 + v4
        subtract: v1 - v4
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
