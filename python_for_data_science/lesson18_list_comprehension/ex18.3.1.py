# Задача 1. Список чётных чисел
#
# Пользователь вводит два числа: А и В. Реализуйте код, который генерирует список из чётных чисел в диапазоне от А до B. Используйте list comprehensions (как и в следующих задачах).

left_border = int(input("Enter left border: "))
right_border = int(input("Enter left border: "))

odds_list = [x for x in range(left_border, right_border + 1) if x % 2 == 0]

print(odds_list)