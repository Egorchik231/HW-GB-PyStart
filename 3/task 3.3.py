def my_func(a, b, c):
    max = a + b
    if a + c > a + b:
        max = a + c
    elif b + c > a + b:
        max = b + c
        if a + c > b + c:
            max = a + c
    print(max)

a = int(input('enter a'))
b = int(input('enter b'))
c = int(input('enter c'))

my_func(a, b, c)
