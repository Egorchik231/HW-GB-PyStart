products = []
quantity = int(input('How many products do you want to add? '))

i = 1
while i <= quantity:
    name = input('Enter name: ')
    price = input('Enter price: ')
    q2 = input('Enter quantity: ')
    tp = input('Enter unit: ')
    tpl = (i, {'название': name, 'цена': price, 'количество': q2, 'eд': tp})
    products.append(tpl)
    i += 1

statisticks = {'название':[], 'цена':[], 'количество':[], 'eд':[]}

for tpl in products:
    i=0
    for k in statisticks.keys():
        statisticks[k].append(tpl[1][k])






print(products,'\n',statisticks)

