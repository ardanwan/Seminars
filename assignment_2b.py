"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """Return a dict with lowercase string of string_1, uppercase string of string_2 and combined string of str1, str2

    :param string_1: string you want to lower its case
    :param string_2: string you want to upper its case
    :return: lowercase str1, uppercase str2 and combined str1&str2 in a dict

    >>> function_2b('hello','world')
    {'L': 'hello', 'U': 'WORLD', 'C': 'helloworld'}
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
