# Using global variable

x = 'global x'


def test():
    y = 'local y'

    print(y)


test()
print(x)

# Local variable & Scope


def test(z):
    print(z)

    test('local z')
    print(z)

# Nested Function


def outer():
    a = 'outer a'

    def inner():
        a = 'inner a'
        print(a)

    inner()
    print(a)


outer()
