class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")

class BoeingEngine:
    def start(self):
        print("Starting Boeing Engine")


# Dynamically we can pass any type of object and that can be used within that class or object at runtime
airbus = AirbusEngine()

fa = Flight(airbus)
fa.startEngine()

boeing = BoeingEngine()
fb = Flight(boeing)
fb.startEngine()
