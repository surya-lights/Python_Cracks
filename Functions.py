# Calling a Function
def my_function():
    print("Hello from a function")


my_function()

# This function expects 2 arguments and gets 2 arguments


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Marc", "Jack")

# If the number of arguments is unknown, add a (* args) before the parameter name


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# If the number of keyword arguments is unknown, add a double (** kwargs) before the parameter name


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# To get a return value, use the return statement


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
