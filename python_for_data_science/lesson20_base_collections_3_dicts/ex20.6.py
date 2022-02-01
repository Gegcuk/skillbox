def ex20_6_1():
    # Задача 1. Песни 2
    # Мы продолжаем писать приложение для удобного прослушивания музыки, но теперь наши песни хранятся в виде словаря,
    # а не вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.
    violator_songs = {
        'World in My Eyes': 4.86,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.9,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.20,
        'Policy of Truth': 4.76,
        'Blue Dress': 4.29,
        'Clean': 5.83
    }
    # Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен,
    # а на экран выводит общее время их звучания.
    #
    # Пример:
    # Сколько песен выбрать? 3
    # Название 1 песни: Halo
    # Название 2 песни: Enjoy the Silence
    # Название 3 песни: Clean
    #
    # Общее время звучания песен: 14.93 минут
    songs_number = int(input('Enter number of songs: '))
    total_time = 0.0
    for i_song in range(songs_number):
        song_name = input('Enter the name of the song: ')
        total_time += violator_songs.get(song_name, 0.0)
    print('Total time of songs: {}'.format(round(total_time, 2)))


def ex20_6_2():
    # Задача 2. География
    # Антон помимо программирования также увлекается и географией, поэтому он решил связать эти две области и написать
    # для своего проекта небольшую программу-навигатор.
    #
    # Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся,
    # в одну строку. Затем пользователь вводит три названия городов. Реализуйте такую программу и для каждого из трёх
    # городов укажите, в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.
    #
    # Пример:
    # Кол-во стран: 2
    # 1 страна: Россия Москва Петербург Новгород
    # 2 страна: Германия Берлин Лейпциг Мюнхен
    #
    # 1 город: Москва
    # Город Москва расположен в стране Россия.
    #
    # 2 город: Мюнхен
    # Город Мюнхен расположен в стране Германия.
    #
    # 3 город: Рим
    # По городу Рим данных нет.
    number_of_countries = int(input("Enter number of countries: "))
    countries_and_cities = dict()
    for i in range(number_of_countries):
        countries_and_cities_list = input('{} country: '.format(i + 1)).split()
        countries_and_cities[countries_and_cities_list[0]] = countries_and_cities_list[1:]
    for i in range(3):
        city = input('Enter {} city: '.format(i + 1))
        is_found = False
        for country in countries_and_cities.keys():
            if city in countries_and_cities[country]:
                print('City {} is in {}.'.format(city, country))
                is_found = True
        if not is_found:
            print('No data about {}'.format(city))

