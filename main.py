def generate_divisible_by_five(n):  # Определяем функцию generate_divisible_by_five, которая принимает один аргумент n.
    return [number for number in range(1, n+1) if number % 5 == 0]  # Используем генератор списка для создания списка чисел от 1 до n, которые делятся на 5.
n = int(input("Введите число n: "))  # Запрашиваем ввод числа n и преобразуем его в целое число.
print(generate_divisible_by_five(n))  # Вызываем функцию generate_divisible_by_five с аргументом n и выводим результат.