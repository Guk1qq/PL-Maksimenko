def swap(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_element = float('-inf')    # max_element инициализируется как отрицательная бесконечность, чтобы гарантировать, что любой элемент матрицы будет больше этой начальной величины.
    max_row, max_col = 0, 0

    # Поиск максимального элемента
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_row, max_col = i, j
                
    # Временное значение для обмена
    temp = matrix[0][0]
    matrix[0][0] = max_element
    matrix[max_row][max_col] = temp

    return matrix

# Пример использования
matrix = [
    [3.0, 2.9, 5.2],
    [7.1, 2.1, 9.1],
    [8.8, 5.8, 10.9]
]

result = swap(matrix)

# Вывод результата
for row in result:
    print(row)
