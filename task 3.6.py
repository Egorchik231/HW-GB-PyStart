def int_func_full(str = 'nosrting'):
    a = str.split(sep = ' ')
    nstr = ''
    for item in a:
        item = int_func(item)
        nstr += item + " "
    print(nstr)

def int_func(stri):
    a = list(stri)
    a[0] = a[0].upper()
    nstr = ''
    for item in a:
        nstr += item

    return nstr

str = input('enter string: ')

int_func_full(str)
