"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Argument:
    - w : first integer
    - x : second integer
    - y : third integer
    - z : fourth integer

    Returns:
    results -- A dictionary with the following keys:
    - 'multiply': containing the product of x * y
    - 'divide'  : the division of x / y
    - 'add'     : the result of w + z
    - 'subtract': the result of w - z
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
