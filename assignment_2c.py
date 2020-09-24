"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """return a dict with multiplication, division, addition, subtraction by given 4 inputs

    :param w: parameter that add z or minus z
    :param x: parameter that multiply y or divided by y
    :param y: parameter that multiply x or divide x
    :param z: parameter that is added to w or subtrated by w
    :return: a dict with four pair key and value: multiplication, x * y; division, x / y; addition, w + z; subtraction, w - z

    >>> function_2c(1,2,4,8)
    {'multiply': 8, 'divide': 0.5, 'add': 9, 'subtract': -7}
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
