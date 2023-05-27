try:
    list_len = int(input('Введите длину массива: '))
    my_list = []

    for i in range(list_len):
        my_list.append(int(input(f'Введите {i + 1} значение: ')))

    x_number = int(input('Введите число для поиска: '))

    print(f'Число встречается {my_list.count(x_number)} раз(а)')

except ValueError:
    print('Введенное значение недействительно')
    exit()



