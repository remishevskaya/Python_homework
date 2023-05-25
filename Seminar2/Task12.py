number_x =
try:
    coins = int(input('Введите количество монеток: '))
except ValueError:
    print('Введенное количество недействительно')
    exit()