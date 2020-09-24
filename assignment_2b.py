"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Function takes two strings, transforms string1 to lowercase, string2 to uppercase. It uses both strings to create a combined string
    string1 + string2. Returns dictionary containing three keys:
    "L" for the lowercase strings
    "U" for the uppercase strings
    "C" for the combined strings
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
