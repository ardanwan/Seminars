from assignment_2b import function_2b
from assignment_2c import function_2c
"""
Used the imported functions (function_2b and function_2c) and the documentation
provided by your teammates to generate the correct answers below. You can use
the following numbers and strings as input for the 2 functions:
[5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']
Run the script to see if you succeeded! PS: Multiple combinations are possible,
just give a correct one.
"""

'''
function_2b(string1, string2):
	Takes in 2 strings as arguments.

	Returns a dict with 3 strings as values. 
		Transforms string1 into lowercase strings.
		Transforms string2 into uppercase strings
		Combines String 1 and 2 together.
		Puts them in a dict with keys "L" for lower, "U" for upper and "C" for combined


function_2c(w, x, y, z):
	takes in 4 integer arguments, w, x, y, z.
	Returns a dict with 4 integers as values.:
		the keyse are: "multiply", mulltiplies x with y.
		"divide", divides x by y.
		"add", Add z to w.
		"subtract", Subtracts z from w.

'''


var_1 = function_2b(...)

var_2 = function_2c(...)

var_3 = str(function_2b(...)) + function_2c(...)

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
    print("Excellent!")
