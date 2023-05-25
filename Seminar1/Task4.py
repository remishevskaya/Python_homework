choko_n = int(input('Введите количество долек шоколадки по горизонтали: '))
choko_m = int(input('Введите количество долек шоколадки по вертикали: '))
choko_k = int(input('Введите количество долек, которые хочется отломить: '))

if choko_k == choko_m * choko_n:
    print('Отломить не получится, это и есть вся шоколадка :)')
elif choko_k < choko_m * choko_n and (choko_k % choko_m == 0 or choko_k % choko_n == 0):
    print('Да, отломить кусочек можно')
else:
    print('Отломить кусочек нельзя')