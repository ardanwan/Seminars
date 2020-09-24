from assignment_2b import function_2b
from assignment_2c import function_2c

print(function_2b.__doc__)
print(function_2c.__doc__)

"""
Used the imported functions (function_2b and function_2c) and the documentation
provided by your teammates to generate the correct answers below. You can use
the following numbers and strings as input for the 2 functions:
[5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']
Run the script to see if you succeeded! PS: Multiple combinations are possible,
just give a correct one.
"""

string1 = "Seminars"
string2 = "CLS"
w = 5
x = 10
y = 1000
z = -50

var_1 = function_2b(string1, string2)

var_2 = function_2c(w, x, y, z)

var_3 = str(function_2b(string1, string2)) + str(function_2c(w,x,y,z))

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
    print("Excellent!")
