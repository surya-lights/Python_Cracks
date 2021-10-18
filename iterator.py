# return an iterator from a tuple and print each value
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# String as an iterator
mystr = "Red"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator
mytuple = ("Gold", "Silver", "Platinum")

for x in mytuple:
    print(x)

# Iterate the characters of the string
mystr = "Diamond"
for x in mystr:
    print(x)

# Iterators that returns number starts from 1 to 5 and sequence increases by one


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        b = self.a
        self.a += 1
        return b


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# To stop iteration


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            b = self.a
            self.a += 1
            return b
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
