# open the file for writing
f = open("myfile.txt", "w")

s = input("Enter text: ")

# write entered text
f.write(s)

# close file
f.close()