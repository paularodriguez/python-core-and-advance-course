from functools import reduce

class Course:

    def __init__(self, name, ratings):
        self.name= name
        self.ratings = ratings

    def average(self):
        # return reduce(lambda x, y: x + y, self.ratings)/len(self.ratings)
        return sum(self.ratings)/len(self.ratings)

c1 = Course("Java", [1,2,3,4,5])

print(c1.name)
print(c1.ratings)
print(c1.average())