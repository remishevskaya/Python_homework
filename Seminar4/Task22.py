try:
    len_first = int(input('Введите количество элементов в первом наборе: '))
    len_second = int(input('Введите количество элементов во втором наборе: '))

    first_list = set()
    second_list = set()

    for i in range(len_first):
        first_list.add(int(input(f'Введите {i + 1} число 1-го множества: ')))
    for i in range(len_second):
        second_list.add(int(input(f'Введите {i + 1} число 2-го множества: ')))

    union_set = first_list.intersection(second_list)
    union_set = list(union_set)
    union_set.sort()

    print(union_set)


except ValueError:
    print('Введенные данные недействительны')
    exit()
