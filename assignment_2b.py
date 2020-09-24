"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Takes as input 2 strings and gives as output a dictionary. The dictionary with
    key "L" gives back the first string in lowercase, the dictionary with key "U"
    gives back the second string in uppercase and the dictionary with key "C" 
    gives a third output which is a combination of both strings
    of both strings
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
