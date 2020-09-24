from assignment_2b import function_2b
from assignment_2c import function_2c
"""
Used the imported functions (function_2b and function_2c) and the documentation
provided by your teammates to generate the correct answers below. You can use
the following numbers and strings as input for the 2 functions:
[5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']
Run the script to see if you succeeded! PS: Multiple combinations are possible,
just give a correct one.

---
function_2b:

Argument:
string_1 -- string
string_2 -- string

Returns:
dict -- dictionary of:
        -- L, lower cased string_1
        -- U, upper cased string_2
        -- C, lower cased string_1 + upper cased string_2

---
function_2c:

Argument:
w, x, y, z -- floats or integers, y != 0

Returns:
results -- dictionary of:
            -- multiply, x * y
            -- divide, x / y
            -- add, w + z
            -- subtract, w - z
"""

var_2 = function_2b("","s")['U'] + function_2b("eminars","B")['C'] + function_2b("orrel","")['L']

var_1 = function_2c(5,95,10,1)['multiply']

var_3 = str(function_2c(10,100,100,10)['multiply']) + function_2b("cls","")['L']


if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
    print("Excellent!")
