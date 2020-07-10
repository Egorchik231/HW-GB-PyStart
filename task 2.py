time = int(input('Введите время в секундах: '))

hh = time//3600
min = (time - hh*60*60)//60
sec = (time - hh*60*60 - min*60)

if len(str(hh)) < 2:
    hh = '0' + str(hh)

if len(str(min)) < 2:
    min = '0' + str(min)

if len(str(sec)) < 2:
    sec = '0' + str(sec)

print(f'{hh}:{min}:{sec}')