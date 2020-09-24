"""
This function has 2 strings as input.
Convert the first string to lower characters and the second string to upper characters.
Combine the two strings.
Return dictionary with variables L (first, lowered string), U (second, capital string)
and C (combined string).
"""
def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
