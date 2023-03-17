numt = input("Ведите номер билета: ")
def sumt(x, i, i_max):
    sum = 0
    while i <= i_max:
        sum += int(x[i])
        i += 1
    return sum
if sumt(numt, 0, 2) == sumt(numt, 3, 5):
    print("Счастливый билет")
else:
    print("Не повезло")