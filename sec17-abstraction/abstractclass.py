from abc import abstractmethod, ABC


# To be an abstract class the class should inherit ABC class from abc module
class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

    # Abstract method
    @abstractmethod
    def drive(self):
        # Pass indicates that we are not implementing this method
        pass


class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print("Starting Three Series")

    def drive(self):
        print("Three Series is being driven")


class FiveSeries(BMW):

    def __init__(self, parkingAssistantEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistantEnabled = parkingAssistantEnabled

    def drive(self):
        print("Five Series is being driven")


bmw = ThreeSeries(True, "BMW", "328i", "2019")
bmw.start()
bmw.drive()

bmw5 = FiveSeries(True, "BMW", "500", "2019")
bmw5.drive()

# An abstract class can't be instantiated
# b = BMW("BMW", "328i", "2019")
