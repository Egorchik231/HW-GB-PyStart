with open('text_3.txt', 'r', encoding='utf-8') as op_tex:
    read = op_tex.readlines()
    aver = 0
    for i in read:
        a = i.split()
        if float(a[1]) >= 20000:
            print(a[0])
        aver += float(a[1])

    aver /= len(read)
    print('Average summary:', aver)