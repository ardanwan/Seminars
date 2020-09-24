"""
Function to multiply, add, substract or divide numbers
input:
w, x, y, z: int or float

returns: dictionary wih the product and quotient of x and y respectively,
sum and difference of w and z respectively
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
