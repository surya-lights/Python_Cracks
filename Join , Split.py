# Join Method
courses = ['History', 'Math', 'Science', 'English']

courses_str = '-' . join(courses)
print(courses_str)

# Split Method
courses = ['History', 'Math', 'Science', 'English']
courses_str1 = ',' . join(courses)
new_list = courses_str1.split('-')
print(courses_str1)
print(new_list)
