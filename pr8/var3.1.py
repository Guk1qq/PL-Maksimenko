def is_symmetric(matrix):   #на вход функции поступает квадратная матрица
    n = len(matrix)  
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

#проверим работу кода данной матрицей, ответ должен быть 'True'
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

print(is_symmetric(matrix))  

matrix = [
    [1, 4, 3],
    [2, 4, 5],
    [3, 4, 6]
]

print(is_symmetric(matrix))  #вывод: выведет уже 'False'



