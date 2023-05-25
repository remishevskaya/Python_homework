cranes = int(input('Введите количество журавликов, сделанных детьми: '))

check = False
crane = 1

while crane != cranes:
    if crane * 2 + (cranes - crane * 2) == cranes and cranes - crane * 2 == crane * 4:
        Petya_crane = crane
        Serezha_crane = crane
        Katya_crane = cranes - crane * 2
        check = True
        print(f'Количество журавликов Пети: {Petya_crane} \nКоличество журавликов Сережи: {Serezha_crane} \n'
              f'Количество журавликов Кати: {Katya_crane}')
    crane += 1

if not check:
    print('Соответствующих комбинаций чисел нет')