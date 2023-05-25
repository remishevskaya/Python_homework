number = int(input('Введите трехзначное число: '))

sum = 0

while number > 0:
    sum = sum + number % 10
    number = number // 10

print(f'Сумма цифр введенного числа равна {sum}')
