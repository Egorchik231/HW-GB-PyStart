revenue = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))

if revenue > cost:
    profit = revenue - cost
    print('Фирма работает в прибыль')
    profitability = profit / revenue
    pers = int(input('Введите количество сотрудников: '))
    profit_per_pes = profit / pers
    # В задании не сказано выводить значение
    # рентабельности и прибыли в расчёте на сотрудника
    # print(f'Рентабельность составляет {profitability},/n
    # а прибыль на сотрудника {profit_per_pes}')

else:
    print("Фирма работает в убыток")