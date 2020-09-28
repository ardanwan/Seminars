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

var_1 = function_2c(x=5, y=5, w=1000, z=50)
var_1 = var_1['subtract']


var_2 = function_2b('Seminars', 'Borrel')
var_2 = var_2['C']
print(var_2)

var_3 = str((function_2c(x=10, y=1000, w=5, z=5))['multiply']) + function_2b('cls', 'CLS')['L']

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
    print("Excellent!")
