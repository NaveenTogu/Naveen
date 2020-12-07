from abc import ABC, abstractmethod

class Animals(ABC):
    @abstractmethod
    def show(self):
        pass

class Human(Animals):
    @abstractmethod
    def show(self):
        pass
class Biker(Human):
    def show(self):
        print('Bike riding and repairing')

class Chef:
    def show(self, d1):
        print('COOK AND BAKE')
        d1.show()


class Designer:
    def show(self):
        print("Arranging")

b1 = Biker()
c1 = Chef()
d1 = Designer()
c1.show(d1)
