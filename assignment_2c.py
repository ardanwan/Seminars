"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Create a dict with the product of x and y,
    the division of x and y,
    the sum of w and z
    and the difference between w and z

    Input
    ---------
    w, x, y, z: numbers (float/int)


    Returns
    ---------
    - Dict with key, value pairs
      "multiply" => x*y
      "divide" => x/y
      "add" => w+z
      "subtract" => w - z
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
