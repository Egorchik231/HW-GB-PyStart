this_li = []
i = int(input('How many elements do you wnat to enter? '))
a = i
while a > 0:
    this_li.append(input('Enter element to put it to list: '))
    a -= 1

q = 0

res_li = []
while q <= i - 2:
    res_li.append(this_li[q + 1])
    res_li.append(this_li[q])
    q += 2
if len(this_li)%2 != 0:
    res_li.append(this_li[i-1])




print(res_li)
