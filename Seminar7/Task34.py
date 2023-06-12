phrase = input('Введите стих Винни-Пуха: ').split()

vow = 'АИОУЫЭЕЁЮЯ'


def count_vow(text):
    count = 0
    for i in text:
        if i.upper() in vow:
            count += 1
    return count


def rithm(func, list_vol):
    if func(list_vol):
        return 'Парам пам-пам'
    return 'Пам парам'


list_rithm = list(map(count_vow, phrase))
print(rithm(lambda x: True if len(set(list_rithm)) == 1 else False, list_rithm))
