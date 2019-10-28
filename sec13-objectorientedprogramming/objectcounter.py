class ObjectCounter:

    numberOfObjects= 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)



oc1 = ObjectCounter()
oc2 = ObjectCounter()
oc3 = ObjectCounter()
ObjectCounter.displayCount()

