from assignment_2b import function_2b
from assignment_2c import function_2c

# print(function_2b.__doc__)
# print(function_2c.__doc__)

"""
Used the imported functions (function_2b and function_2c) and the documentation
provided by your teammates to generate the correct answers below. You can use
the following numbers and strings as input for the 2 functions:
[5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']
Run the script to see if you succeeded! PS: Multiple combinations are possible,
just give a correct one.
"""

string1 = "Seminars"
string2 = "Borrel"
string3 = "CLS"
a = 5
b = 10
c = 1000
d = -50

var_1 = function_2c(c, 1, 1, d)["add"]

var_2 = function_2b(string1, string2)["C"]

var_3 = str(function_2c(a,b,c,d)["multiply"]) + str(function_2b(string3, string2)["L"])

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")
    
if var_3 == "10000cls":
    print("Excellent!")
