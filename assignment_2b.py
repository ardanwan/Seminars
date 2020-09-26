"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""

def function_2b(string_1, string_2):

	"""
	Documentation function_2b:
		Input:
		We take as input two arguments string_1 and string_2.

	Code/Output:
		We create a dictionary which will contain three different keys with each its own corresponding value.
		https://www.w3schools.com/python/python_dictionaries.asp

		key 1: "L", key 2: "U", key 3: "C"

		The values are the variables which we created in the code:
		value 1: the lower case of string_1
		value 2: the upper case of string_2
		value 3: the sum of string_1 and string_2

		This dictionary is returned as the output.
	"""

	lower = string_1.lower()
	upper = string_2.upper()
	combined = string_1 + string_2
	dict = {"L": lower,
               "U": upper,
               "C": combined}

	return dict



