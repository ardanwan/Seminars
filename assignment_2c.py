"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""

def function_2c(w, x, y, z):
    """
    Documentation function_2c:
    	Input:
    		We take as input four arguments w, x, y. z.
    
    	Code/Output:
    		We create a dictionary which will contain four different keys with each its own corresponding value.
    		https://www.w3schools.com/python/python_dictionaries.asp
    
    		key 1: "multiply", key 2: "divide", key 3: "add", key 4: "subtract"
    
    		The values are the variables which we created in the code:
    		value 1: x*y
    		value 2: x/y
    		value 3: w+z
    		value 4: w-z
    
    		This dictionary is returned as the output.
    """
    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results



