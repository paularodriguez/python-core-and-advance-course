import pickle

f = open("student.dat", "rb")
obj = pickle.load(f)

# Call display method from student
obj.display()