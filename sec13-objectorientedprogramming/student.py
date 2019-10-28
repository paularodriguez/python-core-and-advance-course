# Define a static field

class Student:
    # Static field: CSI= Computer Science Engineering
    major = 'CSI'

    def __init__(self, rollno, name):
        self.rollno= rollno
        self.name = name

s1 = Student(1, "Paula")
s2 = Student(2, "Maria")

print(s1.major)
print(s1.name)
print(s1.rollno)

print(s2.major)
print(s2.name)
print(s2.rollno)

#Another way

print(Student.major)



