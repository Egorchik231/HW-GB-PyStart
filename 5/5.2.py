with open('text_forT2.txt', 'r', encoding='utf-8') as op_fil:
    op_fil.seek(0)
    mli = op_fil.readlines()
    if mli[len(mli) - 1].find('\n') != -1:
        num_str = len(mli) + 1
    else:
        num_str = len(mli)
    print('number of string:', num_str)

    op_fil.seek(0)
    line = 1
    for i in mli:
        print('There are(is)', len(i.split()), 'word(s) in line', line)
        line += 1
    if num_str == line:
        print('There is no word in line', line)
