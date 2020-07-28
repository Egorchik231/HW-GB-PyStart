from sys import argv

time, rub_p_h, bonus = argv[1:]

summary = (int(time) * int(rub_p_h)) + int(bonus)
print(summary)