class Matrix:
    def __init__(self, line_s):
        self.lines = line_s

    def __str__(self):
        a = ''
        for i in self.lines:
            b = ''
            for el in i:
                b += str(el) + ' '
            a += b + '\n'
        return a

    def __add__(self, other):
        self.li = []
        i = 0
        if len(self.lines) < len(other.lines):
            a = len(other.lines) - len(self.lines)
            while a > 0:
                self.lines.append([el - el for el in other.lines[len(other.lines) - a]])
                a -= 1

        if len(self.lines) > len(other.lines):
            a = len(self.lines) - len(other.lines)
            while a > 0:
                other.lines.append([el - el for el in self.lines[len(self.lines) - a]])
                a -= 1

        while i < len(self.lines) or i < len(other.lines):
            i_2 = 0
            self.li.append([])
            while i_2 < len(self.lines[i]) or i_2 < len(other.lines[i]):
                self.li[i].append(self.lines[i][i_2] + other.lines[i][i_2])
                i_2 += 1
            i += 1
        return Matrix(self.li)


ob = Matrix([[1, 2, 3], [3, 2, 1], [2, 3, 1], [4, 17, 2]])
print(ob)

ob2 = Matrix([[9, 8, 7], [7, 8, 9], [8, 7, 9]])

print(ob + ob2)
