class MyExcept(Exception):

    def __init__(self, txt):
        self.txt = txt


a = int(input('Enter to number for division: '))
b = int(input('Enter to number for division: '))
try:
    print(a / b)
    if b == -1:
        raise MyExcept('Second numb eq -1. ok')
except ZeroDivisionError:
    print('b == 0!!!')

except MyExcept as my:
    print(my)