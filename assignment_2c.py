"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Argument:
    w, x, y, z -- 4 random numbers

    Returns:
    "multiply": multiplication of the second and third input numbers
    "divide": division of the second input argument by the third input argument
    "add": addition of the first and last input arguments
    "subtract": last input argument subtracted from the first input argument 
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
