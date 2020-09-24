"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Returns a dict conaining the first parameter, converted to lower case, the
    second parameter to upper and the two input string appended after one another.

    @param String first input string, will be converted to lower case
    @param String second input string, will be converted to upper case
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
