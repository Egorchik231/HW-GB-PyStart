def func():
    summ = 0
    t = 1
    while t:
        str = input('enter your string ***if you want stop the prog enter "stop": ')
        a = str.split(sep = ' ')
        for item in a:
            if item != 'stop':
                if item == '':
                    continue
                else:
                    summ += int(item)
            else:
                t = 0
        print(summ)



func()