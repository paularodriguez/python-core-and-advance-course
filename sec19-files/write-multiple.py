# open the file for writing
f = open("myfile.txt", "w")

print("Enter text (Type # when you are done)")

s = ''
while s != '#':
    # write entered text
    s = input()
    f.write(s + "\n")

# close file
f.close()