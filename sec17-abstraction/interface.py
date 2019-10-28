# An interface is an abstract clase with all methods as abstract methods

from abc import abstractmethod, ABC


# To be an abstract class the class should inherit ABC class from abc module
class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        print("Starting Three Series")

    def stop(self):
        print("Stopping Three Series")

    def drive(self):
        print("Three Series is being driven")

class FiveSeries(BMW):

    def __init__(self, parkingAssistantEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistantEnabled = parkingAssistantEnabled

    def start(self):
        print("Starting Five Series")

    def stop(self):
        print("Stopping Five Series")

    def drive(self):
        print("Five Series is being driven")

bmw = ThreeSeries(True, "BMW", "328i", "2019")
bmw.start()
bmw.drive()

bmw5 = FiveSeries(True, "BMW", "500", "2019")
bmw5.drive()

