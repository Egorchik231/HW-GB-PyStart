with open('first_text.txt', 'w+', encoding='utf-8') as op_first:
    inp = ' '
    while inp != '':
        inp = input('Введите что-нибудь: ')
        op_first.write(inp + '\n')
