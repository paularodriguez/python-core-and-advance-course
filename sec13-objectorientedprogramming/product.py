class Product:
    # two __
    def __init__(self):
        self.name = "iPhone"
        self.description = "It's awesome"
        self.price = 1200

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

p1 = Product()
p1.display()