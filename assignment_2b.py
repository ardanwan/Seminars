"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Create a dict with uppercase of string_1, lowercase
    of string_2, and a joined string both.

    Input
    --------
    - string_1: string
    - stirng_2: string

    Returns
    --------
    - Dict with keys "L", "U", "C", denoting values
      "U" => string_1 lowercased
      "L" => string_2 uppercased,
      "C" => both strings combined
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
