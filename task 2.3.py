month = int(input('Enter your month: '))
di = {1: 'winter', 2: 'winter',12: 'winter', 6 : 'summer', 7 : 'summer', 8 : 'summer', 9 : 'autumn', 10 : 'autumn', 11 : 'autumn', 3 :'spring', 5 :'spring', 4 :'spring'}
print(di[month])

li = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer','summer','summer', 'autumn','autumn','autumn', 'winter']
print(li[month - 1])