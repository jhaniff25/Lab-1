first_name="Jasmine"
first_statement= ",this is my first print statement"
first_statement01= ",this is my first print statement #1"
first_statement02= ",this is my first print statement #2"
first_statement03= ",this is my first print statement #3"
mult_var=()
div_var=()
results=(101% 4)
INDENT02=(" "*2)
INDENT03=(" "*8)


print("Hi my name is " +  first_name + ",this is my first print statement")

print("Hi my name is " + first_name + first_statement)

print(f"Hi my name is {first_name}{first_statement}")


print("\n")
print(f"Hi my name is {first_name}{first_statement01}.") 

print("\n")
print(f"{INDENT02} Hi my is {first_name}{first_statement02}.")

print("\n")
print(f"{INDENT03} Hi my name is {first_name}{first_statement03}.")


def multiply(a,b):
    return a*b
mult_var = multiply(24,30)

print(mult_var)

print("There are 720 hours in the month of September.")
print("There are 30 days in September.")

def divide(a,b):
    return a/b
div_var= divide(101,4)

print(div_var)
print(results)
print(f"101/4 is 25, the remainder is {results}")
