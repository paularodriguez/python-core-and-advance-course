class Car:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:

        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine starting")


c = Car("VW", 2015)
e = c.Engine(1)
e.start()