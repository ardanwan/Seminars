"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Multiply x with y
    Divide x with y
    Add w with z
    Substract z to w
    :param w: integer
    :param x: integer
    :param y: integer
    :param z: integer
    :return: dictionnary with the results of the 4 operation, named respectively: multiply, divide, add, substract.
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
