"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    
    """
    Takes in two strings (string_1, string_2.
    Returns dict with:
        dict[0] = string_1 as lower case
        dict[1] = string 2 as upper case
        dict[2] = string_1 as lower case + string_2 as higher case
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
