from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, V=float(0), H=0):
        self.V = V
        self.H = H
        self.name = 'suit' if V == 0 else 'coat'



    @abstractmethod
    def count_area(self):
        return (self.V / 6.5 + 0.5) if self.H == 0 else (2 * self.H + 0.3)


    def count_suit(self):
        return 2 * self.H + 0.3

    def count_coat(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H
        self.name = 'suit'

    def count_suit(self):
        return 2 * self.H + 0.3

    @property
    def count_area(self):
        return (self.V / 6.5 + 0.5) if self.H == 0 else (2 * self.H + 0.3)


class Coat(Clothes):
    def count_coat(self):
        return self.V / 6.5 + 0.5

    @property
    def count_area(self):
        return (self.V / 6.5 + 0.5) if self.H == 0 else (2 * self.H + 0.3)



suit = Suit(15)
print(suit.count_area)

coat = Coat(6.5)
print(coat.count_area)
