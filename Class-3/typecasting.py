name="penguin"
age=15
is_bird=True
weight=40.34

print("datatype of name: ", type(name))
# age-> integer
# integer -> string
print("datatype of age: ", type(age)) 
print("datatype of is_bird: ", type(is_bird))
print("datatype of weight: ", type(weight))

print("\n After Typecasting")
age=str(age)
print(age)
print("datatype of age is:", type(age))
# float-> integer
weight=int(weight)
print(weight)
print("datatype of weight is:", type(weight))