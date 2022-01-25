def ex19_2_1():
    # Задача 1. Заказ
    # После того, как человек сделал заказ в интернет-магазине, ему на почту приходит оповещение с его именем и номером заказа.
    # Напишите программу, которая получает на вход имя и код заказа, а затем выводит на экран соответствующее сообщение. Для решения используйте строковый метод format.
    #
    # Пример:
    # Имя: Иван
    # Номер заказа: 10948
    #
    # Здравствуйте, Иван! Ваш номер заказа: 10948. Приятного дня!
    name = input('Enter your name: ')
    order_code = input('Enter your order code: ')
    message = 'Hello, {}! Number of your order is: {}'.format(name, order_code)
    print(message)
    message = 'Hello, {0}! Number of your order is: {1}'.format(name, order_code)
    print(message)
    message = 'Hello, {name}! Number of your order is: {order_code}'.format(name=name, order_code=order_code)
    print(message)
    message = f'Hello, {name}! Number of your order is: {order_code}'
    print(message)


def ex19_2_2():
    # Задача 2. Долги
    #
    # Один наш друг занял у нас определённую сумму денег и всё никак не может их вернуть. А деньги нам нужны. Поэтому мы
    # решили написать небольшой скрипт-напоминалку, который, возможно, разбудит его совесть.
    # Напишите программу, которая получает на вход имя и долг, а затем выводит на экран сообщение, где имя повторяется
    # несколько раз (и долг, возможно, тоже). Используйте числа в названиях ключей.
    #
    # Пример:
    # Введите имя: Том
    # Введите долг: 100
    # Том! Том, привет! Как дела, Том? Где мои 100 рублей? Том!
    name = input("Enter debtor name: ")
    debt = int(input("Enter loaned amount: "))
    msg = '{name}! Hi, {name}! How are you, {name}? Where is my {debt}$, {name}?'.format(name=name, debt=debt)
    print(msg)


def ex19_2_3():
    # Задача 3. IP-адрес
    # IP-адрес компьютера состоит из 4 чисел, разделённых точкой. Каждое число находится в диапазоне от 0 до 255
    # (включительно).
    #
    # Пример правильного адреса: 192.168.1.0
    # Пример неправильного адреса: 192.168.300.0
    #
    # Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес. Используйте переменную
    # ip_address в
    # качестве шаблона. Обеспечьте контроль ввода.
    ipaddress = []

    def next_part():
        ipaddress_part = int(input('Enter next part: '))
        if ipaddress_part > 255 or ipaddress_part < 0:
            print('Enter correct meaning for IP-part (0 - 255): ')
            ipaddress_part = next_part()
        return ipaddress_part

    for _ in range(4):
        ipaddress.append(next_part())
    ipaddress_total = '{}.{}.{}.{}'.format(ipaddress[0], ipaddress[1], ipaddress[2], ipaddress[3])
    print(ipaddress_total)