"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Argument:
    w, x, y, z -- floats or integers, y != 0

    Returns:
    results -- dictionary of:
                -- multiply, x * y
                -- divide, x / y
                -- add, w + z
                -- subtract, w - z

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
