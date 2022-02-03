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


def ex20_6_3():
    # Задача 3. Криптовалюта
    # При работе с API (application programming interface) сайта биржи по криптовалюте вы получили вот такие данные
    # в виде словаря:
    data = {
        "address": "0x544444444444",
        "ETH": {
            "balance": 444,
            "totalIn": 444,
            "totalOut": 4
        },
        "count_txs": 2,
        "tokens": [
            {
                "fst_token_info": {
                    "address": "0x44444",
                    "name": "fdf",
                    "decimals": 0,
                    "symbol": "dsfdsf",
                    "total_supply": "3228562189",
                    "owner": "0x44444",
                    "last_updated": 1519022607901,
                    "issuances_count": 0,
                    "holders_count": 137528,
                    "price": False
                },
                "balance": 5000,
                "totalIn": 0,
                "total_out": 0
            },
            {
                "sec_token_info": {
                    "address": "0x44444",
                    "name": "ggg",
                    "decimals": "2",
                    "symbol": "fff",
                    "total_supply": "250000000000",
                    "owner": "0x44444",
                    "last_updated": 1520452201,
                    "issuances_count": 0,
                    "holders_count": 20707,
                    "price": False
                },
                "balance": 500,
                "totalIn": 0,
                "total_out": 0
            }

        ]

    }
    # Теперь вам предстоит немного обработать эти данные.
    #
    # Напишите программу, которая выполняет следующий алгоритм действий:
    #
    # Вывести списки ключей и значений словаря.
    # В “ETH” добавить ключ “total_diff” со значением 100.
    # Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
    # Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
    # Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
    for key in data.keys():
        print('{} : {}'.format(key, data[key]))
    data['ETH']['total_diff'] = 100
    print(data['ETH'])
    data['tokens'][0]['fst_token_info']['name'] = 'doge'
    print(data['tokens'][0])
    data['ETH']['totalOut'] = data['tokens'][1].pop('total_out')
    print(data['ETH'], '\n', data['tokens'][1])
    data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
    print(data['tokens'][1]['sec_token_info'])


def ex20_6_4():
    # Задача 4. Товары
    # В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды товаров,
    # второй — за списки количества разнообразных товаров на складе:
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }
    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }
    # Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за 1 шт.).
    #
    # Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.
    #
    # Результат работы программы.
    # Лампа - 27 шт, стоимость 1134 руб
    # Стол - 54 шт, стоимость 27860 руб
    # Диван - 3 шт, стоимость 3550 руб
    # Стул - 105 шт, стоимость 10311 руб
    for product in goods.keys():
        total_quantity = 0
        total_price = 0
        for parameters in store[goods[product]]:
            total_quantity += parameters['quantity']
            total_price += parameters['price'] * parameters['quantity']
        print(f'{product} - {total_quantity} шт., price {total_price} rur.')


def ex20_6_5():
    # Задача 5. Гистограмма частоты 2
    #
    # Мы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз в строке встречается
    # каждый символ. Теперь задача немного поменялась: максимальную частоту выводить не нужно, однако теперь необходимо
    # написать функцию, которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота,
    # а в качестве значения — список символов с этой частотой. Реализуйте такую программу.
    #
    # Пример:
    # Введите текст: Здесь что-то написано
    # Оригинальный словарь частот:
    original_dict = {
        ' ': 2,
        '-': 1,
        'З': 1,
        'а': 2,
        'д': 1,
        'е': 1,
        'и': 1,
        'н': 2,
        'о': 3,
        'п': 1,
        'с': 2,
        'т': 2,
        'ч': 1,
        'ь': 1
    }
    # Инвертированный словарь частот:
    # 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
    # 2 : ['с', ' ', 'т', 'н', 'а']
    # 3 : ['о']
    new_dict = {}
    for key, value in original_dict.items():
        new_dict[value] = new_dict.get(value, [])
        new_dict[value].append(key)
    print(new_dict)

