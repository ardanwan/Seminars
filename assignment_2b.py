"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""


def function_2b(string_1, string_2):

    """

    Args:
        string_1: String converted to lowercase
        string_2: String converted to uppercase

    Returns:
        Dict containing lowercase string_1, uppercase string_2, and combination of string_1 and string_2

    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
            "U": upper,
            "C": combined}

    return dict
