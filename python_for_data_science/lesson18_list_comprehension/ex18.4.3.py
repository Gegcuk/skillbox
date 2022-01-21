# Задача 3. Удаление части
#
# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B). Напишите программу,
# которая удаляет элементы списка с индексами от А до В. Не используйте дополнительные переменные и методы списков.

import random

list_length = int(input("Enter the length of the list: "))
list_for_deleting = [random.randint(0, 1000) for _ in range(0, list_length)]
left_border = random.randint(0, round(list_length/2))
right_border = random.randint(round(list_length/2), (list_length))

print(list_for_deleting)
print(left_border)
print(right_border)
list_for_deleting[left_border:right_border] = []
print(list_for_deleting)
