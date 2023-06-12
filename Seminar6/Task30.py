a_first = int(input('Введите начальный элемент прогрессии: '))
diff = int(input('Введите разность между элементами: '))
elem_count = int(input('Введите количество элементов: '))

result_list = []

for idx, el in enumerate(range(elem_count)):
    result_list.append(a_first + idx * diff)

print(result_list)
