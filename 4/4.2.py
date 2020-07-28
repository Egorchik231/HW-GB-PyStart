import random

my_list = [random.randint(0, 1000) for el in range(1, random.randint(0, 15)) ]

print(my_list)

new_li = []
i = 1

while i < len(my_list):
    if my_list[i] > my_list[i - 1]:
        new_li.append(my_list[i])
    i += 1
print(new_li)