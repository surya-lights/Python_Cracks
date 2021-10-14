class Parent:
    def first(self):
        print('first function')


class Child(Parent):
    def second(self):
        print('second function')


ob = Child()
ob.first()
ob.second()
