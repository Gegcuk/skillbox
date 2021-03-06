import random


def ex1():

# Задача 1. Гласные буквы
#
# Команде лингвистов понравилось качество ваших программ, и они решили заказать у вас функцию для анализатора текста,
# которая создавала бы список гласных букв текста, а заодно считала бы их количество.
#
# Напишите программу, которая запрашивает у пользователя текст и генерирует список из гласных букв этого текста
# (сама строка вводится на русском языке). Выведите в консоль сам список и его длину.
# #
# # Пример:
#
# Введите текст: Нужно отнести кольцо в Мордор!
# #
# # Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
#
# Длина списка: 9

    vowel_letters_list = ['а', 'о', 'у', 'ы', 'и', 'э', 'я', 'ё', 'ю', 'е']
    string_for_check = input('Enter string for searching vowels in: ')
    vowels_in_string = [string_for_check[i_sym] for i_sym in range(0, len(string_for_check)) if
                        string_for_check[i_sym] in vowel_letters_list]
    print(vowels_in_string)
    print(len(vowels_in_string))


def ex2():
    # Задача 2. Генерация
    #
    # Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел, на чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5.
    #
    #
    #
    # Пример:
    #
    # Введите длину списка: 10
    #
    # Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]

    list_length = int(input('Enter the length of the list: '))
    generated_list = [i_sym % 5 if i_sym % 2 != 0 else 1 for i_sym in range(0, list_length)]
    print(generated_list)


def ex3():
    # Задача 3. Случайные соревнования
    #
    # Мы хотим протестировать работу электронной таблицы для участников некоторых соревнований. Есть два списка (то есть две
    # команды), по 20 участников в каждом. В этих списках хранятся очки каждого участника (это вещественные числа с двумя
    # знаками после точки, например 4.03). Участник одной команды соревнуется с участником другой команды под таким же
    # номером. То есть первый соревнуется с первым, второй — со вторым и так далее.
    #
    # Напишите программу, которая генерирует два списка участников (по 20 элементов) из случайных вещественных чисел (от 5
    # до 10). Для этого найдите подходящую функцию из модуля random. Затем сгенерируйте третий список, в котором окажутся
    # только победители из каждой пары.

    ## Пример:#

    # Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
    ## Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
    ## Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]

    first_team = [round(random.uniform(5.00, 10.00), 2) for _ in range(0, 20)]
    second_team = [round(random.uniform(5.00, 10.00), 2) for _ in range(0, 20)]
    result_list = [first_team[i_sym] if first_team[i_sym] > second_team[i_sym] else second_team[i_sym] for i_sym in
                   range(0, 20)]
    print(first_team)
    print(second_team)
    print(result_list)


def ex4():
    # Задача 4. Тренируемся со срезами
    #
    # Дана строка, в которой хранятся первые семь букв английского алфавита.
    #
    # alphabet = 'abcdefg'
    #
    # Напишите программу, которая выводит на экран 10 вот таких результатов:
    #
    # Копия строки.
    # Элементы строки в обратном порядке.
    # Каждый второй элемент строки (включая самый первый).
    # Каждый второй элемент строки после первого.
    # Все элементы до второго.
    # Все элементы, начиная с конца до предпоследнего.
    # Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
    # Последние три элемента строки.
    # Все элементы в диапазоне индексов от 3 до 4 (не включая 5).
    # То же, что и в предыдущем пункте, но в обратном порядке.
    # Для получения и вывода результатов используйте только команду print и срезы.
    #
    # Результаты работы программы:
    #
    # 1: abcdefg
    # 2: gfedcba
    # 3: aceg
    # 4: bdf
    # 5: a
    # 6: g
    # 7: d
    # 8: efg
    # 9: de
    # 10: ed
    alphabet = 'abcdefg'
    print(alphabet)
    print(alphabet[::-1])
    print(alphabet[::2])
    print(alphabet[1::2])
    print(alphabet[:1])
    print(alphabet[6:])
    print(alphabet[3:4])
    print(alphabet[4:])
    print(alphabet[3:5])
    print(alphabet[4:2:-1])


def ex5():
    # Задача 5. Разворот
    #
    # На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. Реализуйте код, который
    # разворачивает последовательность символов, заключённую между первым и последним появлением буквы h, в противоположном
    # порядке.
    entered_string = input("Enter string with 2 'h': ")
    first_h_index = entered_string.index('h')
    second_h_index = entered_string[first_h_index + 1:].index('h') + first_h_index + 1
    result_string = entered_string[:first_h_index] + entered_string[
                                                     second_h_index:first_h_index - 1:-1] + entered_string[
                                                                                            second_h_index + 1:]
    print(result_string)











