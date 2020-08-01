class Cell:
    def __init__(self, number):
        self.cells = number

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells if self.cells - other.cells > 0 else 'Уменьшаемая клетка по площади '
                                                                                  'меньше атакующей')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(round(self.cells / other.cells))

    def make_order(self, n):
        ex = ('*' * n + '\n') * (self.cells // n)
        ex += '*' * (self.cells % n) + '\n'
        return ex


my_cell = Cell(26)
enemy_cell = Cell(10)

print((my_cell / enemy_cell).cells)
print(my_cell.make_order(8))
