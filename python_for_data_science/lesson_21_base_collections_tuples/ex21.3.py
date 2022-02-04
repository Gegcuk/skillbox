def ex21_3_1():
    # Задача 1. Кризис миновал
    # Закупки грейпфрутов прекратились, и кризис в торговой компании закончился. И теперь можно вернуться к обыденным
    # делам. Однако внезапно вы обнаружили, что старый скрипт, который выводит данные о фруктах, куда-то потерялся.
    # Необходимо его восстановить.
    # Дан словарь с парами «название фрукта — цена»:
    incomes = {
        'apple': 5600.20,
        'orange': 3500.45,
        'banana': 5000.00,
        'bergamot': 3700.56,
        'durian': 5987.23,
        'peach': 10000.50,
        'pear': 1020.00,
        'persimmon': 310.00,
    }
    # Вывести на экран словарь в следующем виде:
    #
    # apple -- 5600.2
    # orange -- 3500.45
    # banana -- 5000.0
    # bergamot -- 3700.56
    # durian -- 5987.23
    # peach -- 10000.5
    # pear -- 1020.0
    # persimmon -- 310.0
    #
    # Не используйте обращение по ключу словаря.
    for i_name, i_price in incomes.items():
        print('{name} -- {price}'.format(name=i_name, price=i_price))


def ex21_3_2():
    # Задача 2. Сервер
    # У вас есть данные о сервере, которые хранятся в виде вот такого словаря:
    server_data = {
        "server": {
            "host": "127.0.0.1",
            "port": "10"
        },
        "configuration": {
            "access": "true",
            "login": "Ivan",
            "password": "qwerty"
        }
    }
    # Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно,
    # как они представлены в словаре.
    # Результат работы программы:
    #
    # server:
    #     host: 127.0.0.1
    #     port: 10
    # configuration:
    #     access: true
    #     login: Ivan
    #     password: qwerty
    for i_part, i_data in server_data.items():
        print('{}:'.format(i_part))
        for i_parametr, i_value in server_data[i_part].items():
            print('\t{}: {}'.format(i_parametr, i_value))


