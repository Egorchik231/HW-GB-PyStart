class ComplexNumber:
    def __init__(self, real, complex_part):
        self.real = real
        self.complex_part = complex_part

    def __add__(self, other):
        print ((self.real + other.real), (str(self.complex_part + other.complex_part) + 'j'))

    def __mul__(self, other):
        print ((self.real * other.real - self.complex_part * other.complex_part) + (
                    self.real * other.complex_part + self.complex_part * other.real), 'j', sep='')


com = ComplexNumber(10, 5)
com2 = ComplexNumber(2, 1)

com + com2
com * com2
