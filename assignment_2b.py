"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Return a dictionary with the following key-value pair:
    'L' : Get lower case from string_1.
    'U' : Get upper case from string_2
    'C' : Concatenate string_1 and string_2
    :param string_1: string_1 will be change to lower case
    :param string_2: string_2 will be change to upper case
    :return: dictionary
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
