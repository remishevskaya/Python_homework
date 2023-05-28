try:

    delta_i = 0

    list_len = int(input('Введите длину массива: '))
    my_list = []

    for i in range(list_len):
        my_list.append(int(input(f'Введите {i + 1} значение: ')))

    number = int(input('Введите число для сравнения: '))

    delta = abs(my_list[0] - number)
    delta_i = [0]

    for i in range(len(my_list)):
        if delta > abs(my_list[i] - number):
            delta = abs(my_list[i] - number)
            delta_i[0] = i

    for i in range(len(my_list)):
        if abs(my_list[i] - number) == delta:
            delta_i.append(i)

    print('Самые близкие числа / число: ', end='')
    for i in range(len(delta_i)):
        if i == 0 or my_list[delta_i[i]] != my_list[delta_i[i - 1]]:
            print(my_list[delta_i[i]], end=' ')


except ValueError:
    print('Введенное значение недействительно')
    exit()
