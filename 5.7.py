import json
with open('text_7.txt', 'r', encoding='utf-8') as op_f:
    rd = op_f.readlines()
    avr = 0
    my_di_prof = {}
    my_di_avr = {}
    x = 0
    for i in rd:
        sp = i.split()
        prof = int(sp[2]) - int(sp[3])
        if prof >= 0:
            avr += prof
            x += 1
        my_di_prof[sp[0]] = prof
    avr /= x
    my_di_avr['average_profit'] = avr

with open('text_707.json', 'w+', encoding='utf-8') as js_f:
    json.dump([
        my_di_prof,
        my_di_avr
    ], js_f)
    js_f.seek(0)
