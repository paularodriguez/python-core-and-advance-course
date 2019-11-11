import pickle,student

f = open("student.dat", "wb")
student = student.Student(1, "Paula", 9)

# Arguments: Object to serialize and file
pickle.dump(student, f)
f.close()