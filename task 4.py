number = input('Введите любое положительное целое число: ')

i=0
while i<len(number):
    max = number[0]
    if number[i]>max:
        max = number[i]

    i+=1
print(max)