"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell them the code directly
"""
def function_2b(string_1: str, string_2: str):
    """Function 2b

    Given two strings it will return a dictionary with the following:
        "L" as string_1 lower-cased
        "U" as string_2 upper-cased
        "C" as a cobination of string_1 and string_2

    Args:
        string_1: str
        string_2: str

    Returns: Dict

    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    ret = {
        "L": lower,
        "U": upper,
        "C": combined
    }

    return ret
