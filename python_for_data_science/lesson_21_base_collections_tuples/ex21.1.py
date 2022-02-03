import random
import math


def ex21_1_1():
    # Задача 1. Создание кортежей
    #
    # Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж
    # числами от −5 до 0. Объедините два кортежа, создав тем самым третий кортеж. С помощью метода кортежа определите
    # в нём количество нулей. Выведите на экран третий кортеж и количество нулей в нём.
    first_tuple = tuple([random.randint(0, 5) for _ in range(10)])
    second_tuple = tuple([random.randint(0, 5) for _ in range(10)])
    third_tuple = first_tuple + second_tuple
    print(third_tuple, third_tuple.count(0))


def ex21_1_2():
    # Задача 2. Цилиндр
    # Андрей однажды уже писал функции для расчёта площади сферы и объёма шара. И теперь для своей курсовой работы
    # ему пришлось связаться с цилиндрами.
    #
    # Пользователь вводит два значения: радиус и высоту. Напишите функцию для расчёта площади боковой поверхности
    # цилиндра и его полной площади. Функция должна возвращать два эти значения. После этого в основной программе
    # выводятся оба ответа в две строки.
    radius = float(input('Enter radius of the circle: '))
    height = float(input('Enter height of the cylinder: '))

    def side_surface_and_full_square(radius, height):
        side_surface = 2 * math.pi * radius * height
        full_square = side_surface + 2 * math.pi * radius ** 2
        return side_surface, full_square

    side_surface, full_square = side_surface_and_full_square(radius, height)
    print(round(side_surface, 2), '\n', round(full_square, 2))


