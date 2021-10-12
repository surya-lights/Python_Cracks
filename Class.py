# Create a class named MyClass,

class MyClass:
    x = 5


print(MyClass)

# Creating an object


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)

# Using the __init__() function to assign values for name and age


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Mark", 29)
print(p1.name)
print(p1.age)
