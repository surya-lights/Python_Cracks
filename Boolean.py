# And Operator
user = 'admin'
login = True
if user == 'admin' and login:
    print('admin page')
else:
    print('page cannot be displayed')

# Or Operator
user = 'admin'
login = True
if user == 'admin' or login:
    print('admin page')
else:
    print('page cannot be displayed')

# Not Operator
user = 'admin'
login = False
if not login:
    print('page cannot displayed')
else:
    print('Welcome admin')
