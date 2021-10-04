# To get 'n' for each 'n in nums using List comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = [n for n in nums]
print(my_list)

# 'n*n' for each 'n' in nums (List comprehension)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = [n*n for n in nums]
print(my_list)

# Using Dictionary comprehension
brand = ['Audi', 'Benz', 'BMW']
car = ['A4', 'CLS', 'X6']
my_dict = {brand: car for brand, car in zip(car, brand)}
print(my_dict)

# Using Set comprehension
nums = {1, 1, 2, 3, 4, 3, 5, 6, 7, 8, 7, 9}
my_set = {n for n in nums}
print(my_set)
