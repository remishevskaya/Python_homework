import math

summ = 0
comp = 0

try:
    summ = int(input('Введите сумму чисел: '))
    comp = int(input('Введите произведение чисел: '))

    Diskr = summ ** 2 - 4 * comp

    if Diskr < 0:
        print('Таких чисел нет')
    elif Diskr == 0:
        x = summ // 2
        print(f'Числа X и Y равны и составляют {x}')
    elif Diskr > 0:
        x = (summ + math.sqrt(Diskr)) // 2
        y = (summ - math.sqrt(Diskr)) // 2
        print(f'Число X: {x}  \n Число Y: {y}')

except ValueError:
    print('Введенное количество недействительно')
    exit()
