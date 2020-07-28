import random

my_list = [random.randint(0, 10) for el in range(1, random.randint(10, 20)) ]

print(my_list)
new_li = []
for el in my_list:
    if my_list.count(el) == 1:
        new_li.append(el)

print(new_li)
