"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    # This function takes as input two strings.

    # It transforms the first string to a lower version of itself
    # The second string becomes an upper version of itself.
    # It also combines the two original string into one combined string
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    # The function returns a dictionary, storing the lower under the key L, the upper string under the key U and
    # the combined string under the key C

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
