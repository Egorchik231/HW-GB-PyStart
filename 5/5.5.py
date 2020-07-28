from random import randint
with open('text_5.txt', 'w+', encoding='utf-8') as op_f:

    my_list = [str(randint(0, 1000)) for el in range(1, randint(3, 15))]
    op_f.write(' '.join(my_list))
    op_f.seek(0)
    rd = op_f.read()
    res = 0
    print(rd)
    for i in rd.split():
        res += int(i)

    print(res)
