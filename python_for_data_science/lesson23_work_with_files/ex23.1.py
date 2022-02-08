import os


def ex23_1_0():
    def print_dirs(project):
        print('\nContent of folder: ', project)
        if os.path.exists(project):
            for i_elem in os.listdir(project):
                path = os.path.join(project, i_elem)
                print('    ', path)
        else:
            print('Directory is not exist')

    projects_list = ['skillbox', 'probe', 'testProject1']
    for i_project in projects_list:
        path_to_project = os.path.abspath(os.path.join('..', '..', '..', i_project))
        print_dirs(path_to_project)


def ex23_1_1():
    # Задача 1. Иконки
    #
    # Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его
    # диска: папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой
    # тип иконки вставить.
    #
    # Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь (на
    # директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь указывает
    # на файл, то также выведите его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка пути
    # на существование.
    #
    # Подсказка: для вывода размера файла поищите соответствующий метод.
    #
    # Пример 1:
    # Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
    # Это файл
    # Размер файла: 605 байт
    #
    # Пример 2:
    # Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
    # Указанного пути не существует
    path = input('Enter the path of file: ')
    if os.path.exists(path):
        if os.path.isfile(path):
            print('This file has {} B'.format(os.path.getsize(path)))
        elif os.path.isdir(path):
            print('This is directory')
        elif os.path.islink(path):
            print('This is link')
    else:
        print('File is not exist')



