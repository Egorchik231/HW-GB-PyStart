import functools as ft

my_li = [el for el in range(100, 1001) if el % 2 == 0]
print(my_li)

multipl = ft.reduce(lambda x, y: x * y, my_li)
print(multipl)