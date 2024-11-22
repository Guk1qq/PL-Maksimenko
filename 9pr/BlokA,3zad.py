def reverse_number(n):
    if n < 0:
        return '-' + reverse_number(-n)
    
    # Базовый случай
    if n < 10:
        return str(n)
    
    # Рекурсивный вызов
    return str(n % 10) + reverse_number(n // 10)

# Пример использования
number = 343547534463567
reversed_number = reverse_number(number)

# Вывод результата
print(reversed_number)
