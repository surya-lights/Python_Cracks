# For loop
nums = [0, 1, 2, 3, 4]
for num in nums:
    print(nums)

# To break loop iteration
nums_1 = [5, 6, 7, 8, 9]
for nums_1 in nums_1:
    print(nums_1)
if nums_1 == 4:
    print('Found')
    breakpoint()
    print(nums_1)

# Continue Statement and to skip Iteration
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
