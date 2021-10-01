# Inner loop
nums = [1, 2, 3]
for num in nums:
    for letter in 'abc':
        print(letter, nums)

# Build in function Range
for i in range(10):
    print(i)
for i in range(1, 11):
    print(i)

# While loop
x = 0
while x < 10:
    print(x)
    x += 1
# Break
x = 0
while x < 10:
    if x := 5:
        breakpoint()
        print(x)
        x += 1

# Infinite loop
a = 0
while True:
    print(a)
    a += 1
