# If we don't specify buffer size, 4096 or 8092 will be used by Python VM
f = open("filename", "mode", "buffer")

# Do things and finally, close the file
f.close()

# MODES

# W - WRITE MODE -
# write on the file, if the file has content,
# it will be deleted, new content is written from the beginning of the file

# R - READ MODE -
# to read the file from the beginning

# A - APPEND MODE -
# Append content to the file, current file content is not deleted

# W+ - WRITE AND READ -

# R+ - READ AND APPEND

# A+ - APPEND AND READ

# X - SPECIAL CREATION MODE
# when you open a file in this mode, a new file is created,
# if one file exists with the same name one error is thrown


# BINARY FILES, Append 'b' to the previous modes: ex. wb, rb...