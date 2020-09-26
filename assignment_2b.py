"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
	'''
    Input: Two strings str1, str2
    Return: A dict with following results:

    L: str1 as lowercase
    U: str2 as uppercase
    C: combine str1 + str2
	'''
    
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
