# Ввод числа от пользователя
n = int(input("Введите число n: "))

# Создание генератора списка
spiis5 = [i for i in range(1, n + 1) if i % 5 == 0]

# Вывод списка чисел, которые делятся на 5
print(spiis5)
