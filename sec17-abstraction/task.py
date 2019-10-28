from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling HP")

class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling DELL")


class HPNotebook(HP):
    def click(self):
        print("Clicking HP Notebook")

class DellNotebook(Dell):
    def click(self):
        print("Clicking DELL Notebook")


hpnb = HPNotebook()
hpnb.scroll()
hpnb.click()

dellnb = DellNotebook()
dellnb.scroll()
dellnb.click()

