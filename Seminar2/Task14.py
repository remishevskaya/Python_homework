number = int(input('Введите число: '))

number_two = 2
deg = 0
num_print = 0

while number > num_print:
    num_print = number_two ** deg
    if num_print < number:
        print(num_print)
    deg += 1

