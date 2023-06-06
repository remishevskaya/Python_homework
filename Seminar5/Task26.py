def degree(a, b):
    if b == 0:
        return 1
    b = b - 1
    return degree(a, b) * a


try:

    num_a = int(input('Введите число: '))
    num_b = int(input('Введите степень: '))

    print(degree(num_a, num_b))

except ValueError:
    print('Введенные данные недействительны')
    exit()
