from threading import Thread

class EvenNumbers:

    def displayEvenNumbers(self):
        for i in range (0, 100):
            if i % 2 == 0:
                print(i)

class OddNumbers:

    def displayOddNumbers(self):
        for i in range (0, 100):
            if i % 2 != 0:
                print(i)


e = EvenNumbers()
o = OddNumbers()

t1 = Thread(target=e.displayEvenNumbers)
t1.start()

t2 = Thread(target=o.displayOddNumbers())
t2.start()

for i in range (0,100): print(i)
