# Dictionaries
student = {'name': 'charles', 'age': 25, 'course': ['math', 'Biology']}
print(student)

# Get Method
student = {'name': 'charles', 'age': 25, 'course': ['math', 'Biology']}
print(student.get('name'))

# Adding a new argument
student = {'name': 'charles', 'age': 25, 'course': ['math', 'Biology']}
print(student.get('phone', 'not found'))

# New entry to dictionaries
student = {'name': 'charles', 'age': 25, 'course': ['math', 'Biology'], 'phone': '1234_123'}
print(student.get('phone', 'not found'))
