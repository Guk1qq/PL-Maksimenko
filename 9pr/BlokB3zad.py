def print_odd_indexed(numbers, index=1):
    # Проверяем, если индекс меньше длины списка
    if index < len(numbers):
        print(numbers[index])  # Выводим элемент с нечетным индексом
        print_odd_indexed(numbers, index + 2)  # Рекурсивный вызов с увеличенным индексом

# Пример 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print_odd_indexed(numbers)
