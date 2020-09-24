"""
Function 2b takes two strings as arguments and creates three new strings: str lower which is the first string in lowercase, str upper which is the second string in uppercase, and str combined which is the concatenation of the original first and second strings.

The function then creates a dictionary named "dict" which lists "L" followed by str lower, "U" followed by str upper, and "C" followed by str combined.

The function then returns dict.
"""
def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
