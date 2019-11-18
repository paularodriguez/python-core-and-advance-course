from threading import *


class Display:

    def displayNumbers(self):
        print(current_thread())
        i = 0
        while i <= 10:
            print(i)
            i += 1


# Create instance of class
obj = Display()

# Create thread specifying target
t = Thread(target=obj.displayNumbers)

# Start the thread
t.start()
