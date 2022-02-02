import random


def ex20_4_1():
    # Задача 1. Пунктуация
    #
    # Напишите программу, которая считает количество знаков пунктуации в символьной строке. К знакам пунктуации относятся
    # символы из набора ".,;:!?". Набор должен храниться в виде множества.
    #
    # Пример:
    # Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
    # Количество знаков пунктуации: 6
    set_of_symbols = {'.', ',', ';', ':', '!', '?'}
    symbols_counter = 0
    user_text = input('Enter your text: ')
    for symbol in user_text:
        if symbol in set_of_symbols:
            symbols_counter += 1
    print('Number of punctuation marks: {}'.format(symbols_counter))


def ex20_4_2():
    # Задача 2. Семинар
    #
    # На одном семинаре по теории множеств нужно показать наглядный пример, как эти множества работают.
    # Для начала было сгенерировано два набора чисел:
    #
    nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3,
              1]
    nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21,
              21]
    #
    # Вас попросили написать программу, которая будет наглядно демонстрировать работу со множествами с помощью этих чисел.
    #
    # Напишите программу, которая преобразует списки во множества и убирает повторяющиеся элементы. Затем удаляет
    # минимальный элемент из каждого множества и добавляет туда случайное число в диапазоне от 100 до 200. Затем
    # выполните следующие действия со множествами:
    #
    # Вывести все элементы множеств (объединение).
    # Вывести только общие элементы (пересечение).
    # Вывести элементы, входящие в nums_2, но не входящие в nums_1.
    #
    # Пример результата:
    # 1-е множество: {1, 2, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 24, 26, 27, 29}
    # 2-е множество: {1, 5, 7, 8, 9, 11, 12, 13, 15, 16, 19, 21, 22, 23, 24, 29, 30}
    #
    # Минимальный элемент 1-го множества: 1
    # Минимальный элемент 2-го множества: 1
    #
    # Случайное число для 1-го множества: 126
    # Случайное число для 2-го множества: 169
    #
    # Объединение множеств: {2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 29, 30, 169, 126}
    # Пересечение множеств: {7, 8, 11, 12, 13, 15, 16, 19, 21, 22, 24, 29}
    # Элементы, входящие в nums_2, но не входящие в nums_1: {5, 9, 169, 23, 30}
    set_1 = set(nums_1)
    set_2 = set(nums_2)
    set_1.remove(min(nums_1))
    set_2.remove(min(nums_2))
    print(set_1, '\n', set_2)
    set_1.add(random.randint(100, 201))
    set_2.add(random.randint(100, 201))
    print(set_1.union(set_2))
    print(set_1 | set_2)
    print(set_1.intersection(set_2))
    print(set_1 & set_2)
    print(set_2.difference(set_1))
    print(set_2 - set_1)


def ex20_4_3():
    # Задача 3. Различные цифры
    #
    # Напишите программу, которая находит все различные цифры в символьной строке. Для решения используйте множество
    # (цифры будут различные, и поиск во множестве намного быстрее, чем в списке).
    #
    # Подсказка: можно использовать вот такое сравнение '0'<=x<='9'
    #
    # Пример:
    # Введите строку: ab1n32kz2
    # Различные цифры строки: 123
    user_text = input('Enter your text with numbers: ')
    set_of_numbers = set()
    for symbol in user_text:
        if '0' <= symbol <= '9':
            set_of_numbers.add(symbol)
    print(set_of_numbers)
