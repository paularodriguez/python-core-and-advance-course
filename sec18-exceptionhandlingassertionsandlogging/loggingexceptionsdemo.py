import logging
logging.basicConfig(filename="myLog.log", level=logging.DEBUG)

try:
    file = open("myfile", "w")
    a,b = [int(x) for x in input("Enter two numbers:").split()]
    logging.info("Division in progress")
    c = a/b
    file.write("Writing {0} into file".format(c))
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by zero is not allowed")
else:
    # Useful when we have code that should be executed only when an exception is not thrown
    print("You have entered a non zero number")
finally:
    # This code is executed always
    file.close()
    print("file closed")
print("The program continues here")