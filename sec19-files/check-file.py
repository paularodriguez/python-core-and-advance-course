import os,sys

# file = "myfile.txt"
file = "wrongfile.txt"
if os.path.isfile(file):
    f = open(file, "r")

else:
    print("File does not exist")
    #Exit
    sys.exit()


s = f.read()
f.close()
print(s)