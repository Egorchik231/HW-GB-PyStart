with open('text_4.txt', 'r', encoding='utf-8') as op_f:
    read = op_f.readlines()
    my_li = []
    for i in read:
        if i.split()[2] == '1':
            my_li.append('Один - 1')
        elif i.split()[2] == '2':
            my_li.append('Два - 2')
        elif i.split()[2] == '3':
            my_li.append('Три - 3')
        elif i.split()[2] == '4':
            my_li.append('Четыре - 4')

with open('text_44.txt', 'w', encoding='utf-8') as op_f2:
    op_f2.write('\n'.join(my_li))



#Ещё можно организовать поиск соответствия через словарик,
#это, возможно, было бы компактнее. Но этот способ был первым в моей голове)))

