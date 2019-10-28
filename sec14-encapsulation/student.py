class Student:

    def __init__(self):
        # class fields can be private using two underscores before the name (__)
        self.__id=123
        self.__name="Paula"

    def display(self):
        print(self.__id)
        print(self.__name)


s = Student()
# Using display method
s.display()

# Private fields are not completely hidden -> You can access this way to private fields
# It's call name mangling
print(s._Student__id)
print(s._Student__name)