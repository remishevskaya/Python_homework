berries = input('Введите урожайность кустов через пробел: ').split()

max_berries = 0

for i in range(len(berries) - 1):
    if i == 0:
        max_berries = int(berries[-1]) + int(berries[i]) + int(berries[i + 1])
    elif i == len(berries):
        if int(berries[-2]) + int(berries[-1]) + int(berries[0]) > max_berries:
            max_berries = int(berries[-2]) + int(berries[-1]) + int(berries[0])
    else:
        if int(berries[i]) + int(berries[i + 1]) + int(berries[i - 1]) > max_berries:
            max_berries = int(berries[i]) + int(berries[i + 1]) + int(berries[i - 1])

print(f'Максимальное число ягод, которые можно собрать: {max_berries}')
