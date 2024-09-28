x=5
# if and else -> conditional statement
if(type(x) is int):
    print("true")
else:
    print("false")

# type()-> helps user to identify the type of a variable

x=6.45
if(type(x) is not float):
    print("true")
else:
    print("false")

x=52
y=52
if(x is y):
    print("x & y SAME IDENTITY")
y=30
if(x is not y):
    print("a & y have different identity")
