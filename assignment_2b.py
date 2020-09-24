"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):

    """
    funtion returns a dictionary with keys are L, U and C
    In L string1 is returned as a lower case string, 
    In U string2 is returned as upper case string,
    In C string1 and string2 are combined.
    """
    
    
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
