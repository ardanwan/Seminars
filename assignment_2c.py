"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):

    # Multiply value x with y
    multiplication = x * y
    # Divide value x with y
    division = x / y
    # Add value w with z
    addition = w + z
    # Substract value w with z
    subtraction = w - z

    # Create dict of all results above and return
    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
