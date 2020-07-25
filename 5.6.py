with open('text_6.txt', 'r', encoding='utf-8') as op_f:
    rd = op_f.readlines()
    my_di = {}
    for i in rd:
        sp = i.split()
        res = 0

        for a in sp:
            my_str = ''
            for c in a:
                if c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or \
                        c == '8' or c == '9':
                    my_str += c
            if my_str != '':
                res += int(my_str)

        my_di[sp[0][:len(sp[0]) - 1]] = res
    print(my_di)
