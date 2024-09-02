# Функция для создания нового массива строк, длина которых <= 3
def filter_short_strings(strings):
    # Создаем пустой массив для хранения результатов
    result = []
    
    # Перебираем все строки в исходном массиве
    for string in strings:
        # Если длина строки <= 3, добавляем её в новый массив
        if len(string) <= 3:
            result.append(string)
    
    # Возвращаем новый массив
    return result

# Вводим исходный массив строк с клавиатуры
input_strings = input("Введите строки через пробел: ").split()

# Получаем новый массив строк с длиной <= 3 символа
filtered_strings = filter_short_strings(input_strings)

# Выводим результат
print("Строки длиной <= 3 символов:", filtered_strings)
