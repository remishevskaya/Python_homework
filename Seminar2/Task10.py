coins = 0
coin = 0
coins_upp = 0

try:
    coins = int(input('Введите количество монеток: '))

    if coins < 0:
        print('Количество монеток не может быть отрицательным')
        exit()
    elif coins == 0:
        print('Ничего переворачивать не нужно')
        exit()
    else:
        for i in range(coins):
            coin = int(input('Введите положение монетки (0/1): '))
            if coin > 1 or coin < 0:
                print('Введенное положение недействительно')
                exit()
            if coin == 0:
                coins_upp += 1
        if coins_upp > coins / 2:
            print(f'Количество монеток, которые нужно перевернуть: {coins - coins_upp}')
        elif coins_upp <= coins:
            print(f'Количество монеток, которые нужно перевернуть: {coins_upp}')

except ValueError:
    print('Введенные данные недействительны')
    exit()
