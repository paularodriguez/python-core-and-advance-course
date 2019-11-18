from threading import *


class MyThread(Thread):

    def run(self):
        print(current_thread())
        i = 0
        while i <= 10:
            print(i)
            i += 1


# Create an instance of the subclass
t = MyThread()

# Call start method, not run(). Run is started internally
# If we call t.run() the Main thread will executed the code
t.start()
