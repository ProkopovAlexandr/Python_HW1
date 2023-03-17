num = input('Введите число: ')
sum = 0

for i in range(len(num)):
    try:
        sum += int(num[i])
    except ValueError:
        continue


print(sum)