"""
This function has 4 values (w, x, y and z) as input.
It returns a dictionary with variables "multiply" (x times y), "division" ( x divided by y),
"add" (w and z added) and "subtract" which subtracts w by z.
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
