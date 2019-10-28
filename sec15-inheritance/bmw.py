class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")


# Use brackets to extend
class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        # BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    # Overriding example
    def start(self):
        # Call parent start
        super().start()
        print("Starting the ThreeSeries car")

    def display(self):
        print("Cruise control enabled: ", self.cruiseControlEnabled)


class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        # BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()