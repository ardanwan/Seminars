"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):

    # turn string_1 to lowercase 
    lower = string_1.lower()
    # turn string_2 to uppercase 
    upper = string_2.upper()
    # added strings together
    combined = string_1 + string_2

    # make dictionary of lower upper and combined string and return
    dict = {"L": lower,
               "U": upper,
                "C": combined}
    return dict
