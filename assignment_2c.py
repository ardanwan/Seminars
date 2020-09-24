"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Arguments: w, x, y, and z

    Returns: a dictionary containing keys 'multiply' with value x * y,
                                          'divide' with value x / y,
                                          'add' with value w + z, and
                                          'subtract' with value w - z  
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
