def sum(a, b):
    if b == 0:
        return a
    b -= 1
    return sum(a + 1, b)


try:

    num_a = int(input('Введите число 1: '))
    num_b = int(input('Введите число 2: '))

    print(sum(num_a, num_b))

except ValueError:
    print('Введенные данные недействительны')
    exit()