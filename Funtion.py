# Pass Function

def hello_func():
    pass


hello_func()
print(hello_func())


def hello_func():
    hello_func()


print(hello_func)

# Function allows to reuse ,without repeat


def hello_func():
    print('hello function!')
    hello_func()
