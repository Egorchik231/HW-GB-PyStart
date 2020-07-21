from sys import argv
from itertools import count, cycle
# 1 -----------------

i = 0
start = int(argv[1])
for el in count(start):
    print(el)
    i+=1
    if i > 10:
        break

# 2 -----------------

li = [1, 22, 3, 4, 5]
i = 0
for eli in cycle(li):
    print(eli)
    i+=1
    if i > 15:
        break