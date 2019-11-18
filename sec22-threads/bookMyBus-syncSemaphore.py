from threading import *

class BookMyBus:

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.s = Semaphore()

    def buy(self, seatsRequested):
        # print(current_thread())
        self.s.acquire()

        print("Total seats available: ", self.availableSeats)
        if self.availableSeats >= seatsRequested:
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.availableSeats -= seatsRequested
        else:
            print("Sorry.  No seats available")
        self.s.release()


obj = BookMyBus(10)

t1 = Thread(target=obj.buy, args=(3,)) # We add one comma because it expects one list
t2 = Thread(target=obj.buy, args=(4,))
t3 = Thread(target=obj.buy, args=(5,))

t1.start()
t2.start()
t3.start()