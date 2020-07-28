def fact(n):
    i = 1
    r = 1
    while i <= n:
        r *= i
        yield r
        i += 1


for el in fact(5):
    print(el)
