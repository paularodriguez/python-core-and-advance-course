class Programmer:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, technologies):
        self.technologies = technologies

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName("Paula")
p1.setSalary(50)
p1.setTechnologies(["Java", "Python", "JS"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())

print(Programmer.getName(p1))
print(Programmer.getSalary(p1))
print(Programmer.getTechnologies(p1))
