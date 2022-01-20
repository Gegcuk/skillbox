# Задача 3. Отряды
#
# Мы продолжаем пробовать себя в качестве разработчика игр. Теперь нужно написать небольшую логику поведения некоторых
# отрядов, а также их урон. Есть два отряда, в каждом по 10 монстров. В первом отряде у каждого монстра урон абсолютно
# случайный и колеблется от 50 до 80, а во втором — от 30 до 60. Оба отряда вместе напали на третий, также из 10 юнитов.
# Юнит третьего отряда погибает, если сумма урона от двух монстров больше 100.
#
# Напишите программу, которая генерирует случайные значения в первых двух списках в заданных диапазонах, а также
# генерирует список, состоящий из фраз «Погиб» или «Выжил». Выведите все списки на экран.
#
#
#
# Пример:
#
# Урон первого отряда: [77, 75, 76, 77, 76, 73, 57, 67, 76, 52]
#
# Урон второго отряда: [53, 51, 31, 60, 49, 37, 31, 60, 37, 47]
#
# Состояние третьего отряда: ['Погиб', 'Погиб', 'Погиб', 'Погиб', 'Погиб', 'Погиб', 'Выжил', 'Погиб', 'Погиб', 'Выжил']

import random

first_squad = [random.randint(50, 80) for _ in range(10)]
second_squad = [random.randint(30, 60) for _ in range(10)]

result_squad = ['Dead' if (first_squad[i_warrior] + second_squad[i_warrior]) > 100 else 'Alive' for i_warrior in range(len(first_squad))]
print(result_squad)