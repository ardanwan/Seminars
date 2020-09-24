"""
Function 2c takes four numbers as arguments and performs four operations for which it creates new corresponding variables: multiplication between the 2nd and 3rd arguments, division of the 2nd arg. by the 3rd, addition of the 1st and 4th args., and subtraction of the 1st arg. from the 4th.

The function then creates a dictionary named "results" that lists the four operations followed by their values.

The function then returns results.
"""
def function_2c(w, x, y, z):

    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
