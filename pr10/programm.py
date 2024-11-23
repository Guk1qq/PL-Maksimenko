def read_numbers_from_file(file):
    with open('MaksimenkoAnnaSergeevna_YB-42_vvod.txt', 'r') as file:
        # Читаем строку, разбиваем по пробелам и преобразуем в список чисел
        numbers = list(map(int, file.readline().strip().split()))
    matrix = []
    rows = 3  
    cols = 3 
    for i in range(rows):
        row = numbers[i * cols:(i + 1) * cols]
        matrix.append(row)
    return matrix
def main():
    file = 'MaksimenkoAnnaSergeevna_YB-42_vvod.txt'
    matrix = read_numbers_from_file(file)
    print("матрица:")
    for row in matrix:
        print(row)
    return matrix
a = main()
#обработка "в матрицу" закончена 
def is_symmetric(matrix):   
    n = len(matrix)  
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
matrix = a
result = is_symmetric(matrix)
with open('MaksimenkoAnnaSergeevna_YB-42_vivod.txt', 'w') as f:
    f.write(str(result))
with open('MaksimenkoAnnaSergeevna_YB-42_vivod.txt', 'r') as f:
    iso = f.read()
    print("Результат из файла:", iso)
