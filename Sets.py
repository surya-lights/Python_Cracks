# Sets
cs_courses = {'Math', 'History', 'Chemistry', 'Physics'}
print(cs_courses)
# in function to check the data in set
cs_courses = {'Math', 'History', 'Chemistry', 'Physics', 'Math'}
print('Math' in cs_courses)

# Set, Union Method
cs_courses = {'Math', 'History', 'Biology', 'Physics'}
art_courses = {'Math', 'Art', 'Chemistry', 'Physics'}
print(cs_courses.union(art_courses))

# Set, Difference Method
cs_courses = {'Math', 'History', 'Biology', 'Physics'}
art_courses = {'Math', 'Art', 'Chemistry', 'Physics'}
print(cs_courses.difference(art_courses))

# Set Intersection Method
cs_courses = {'Math', 'History', 'Biology', 'Physics'}
art_courses = {'Math', 'Art', 'Chemistry', 'Physics'}
print(cs_courses.intersection(art_courses))
