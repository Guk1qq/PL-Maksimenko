a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
while a >= b:
    if a % 2 != 0:
        print(a)
        a -= 1
    else:
        a -= 1
