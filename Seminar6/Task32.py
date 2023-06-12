start_list = input('Введите список через пробел: ').split(' ')
min_elem = int(input('Введите минимальное значение элемента: '))
max_elem = int(input('Введите максимальное значение элемента: '))

result_list = [int(el) for el in start_list if (int(el) > min_elem) and (int(el) < max_elem)]

print(result_list)
