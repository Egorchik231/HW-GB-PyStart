def my_func(x, y):
    print(x**y)
def my_func2(x, y):
    while y < 0:
        t = x
        t *= x
        y += 1
    print(1 / t)

x = int(input('x = '))
y = int(input('y = '))

my_func(x, y)
my_func2(x, y)


