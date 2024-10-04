n = int(input('Введите число n: '))
k = 1
s = 0
for i in range(1,n+1):
    k = k * i
    s += k
print(s)
