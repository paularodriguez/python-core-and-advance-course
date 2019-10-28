# Create class Patient with setter and accessor methods, one instance, set and print the fields
class Patient:
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSSN(self, SSN):
        self.SSN = SSN

    def getSSN(self):
        return self.SSN

p = Patient()
p.setId(1)
p.setName("Paula")
p.setSSN(12345)

print(p.getId())
print(p.getName())
print(p.getSSN())