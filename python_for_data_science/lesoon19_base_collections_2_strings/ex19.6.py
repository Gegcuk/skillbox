def ex19_6_1():
    # Задача 1. Меню ресторана
    #
    # Один ресторан заказал вам написать приложение, которое в один клик отображало бы пользователю доступное меню в удобном
    # виде. Для этого ресторан любезно предоставил свой сайт, откуда можно получить актуальную информацию о меню в виде
    # идущих подряд названий.
    #
    # Напишите программу, которая выводит это меню на экран. На вход подаётся строка из названий блюд, разделённых символом
    # «;», а на выходе эти названия перечисляются через запятую и пробел.
    #
    # Пример:
    #
    # Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов
    #
    # На данный момент в меню есть: утиное филе, фланк-стейк, банановый пирог, плов
    menu = input("Enter menu: ").split(";")
    new_menu = ", ".join(menu)
    print(new_menu)


def ex19_6_2():
    # Задача 2. Самое длинное слово
    #
    # Дана строка, содержащая пробелы. Найдите в ней самое длинное слово, выведите это слово и его длину. Если таких
    # слов несколько, выведите первое из них.
    user_text = input('Enter your text: ').split()
    max_word_length = len(user_text[0])
    max_word = user_text[0]
    for i_word in range(len(user_text)):
        if len(user_text[i_word]) > max_word_length:
            max_word = user_text[i_word]
            max_word_length = len(user_text[i_word])
    print("Longest word is - {}. Length = {}".format(max_word, max_word_length))


def ex16_6_3():
    # Задача 3. Файлы
    # В одной IT-компании существует негласный закон об именовании текстовых документов:
    # Название файла не должно начинаться на один из специальных символов: @№$%^&*().
    # Файл заканчивается расширением .txt или .docx.
    #
    # Напишите программу, которая получает на вход полное название файла и проверяет его по этим правилам.
    #
    # Пример 1:
    # Название файла: @example.txt
    # Ошибка: название начинается на один из специальных символов
    #
    # Пример 2:
    #
    # Название файла: example.ttx
    # Ошибка: неверное расширение файла. Ожидалось .txt или .docx
    #
    # Пример 3:
    # Название файла: example.txt
    # Файл назван верно.
    right_symbols = '@№$%^&*()'
    file_path = input("Enter the path: ")
    if file_path[0] in right_symbols:
        print('Ошибка: название начинается на один из специальных символов')
    elif not (file_path.endswith('.txt') or file_path.endswith('.docx')):
        print('Неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('Файл назван верно.')


def ex19_6_4():
    # Задача 4. Заглавные буквы
    #
    # Пользователь вводит строку. Напишите программу, которая изменяет регистр символов в этой строке так, чтобы первая
    # буква каждого слова была заглавной, а остальные буквы — строчными.
    #
    # Пример:
    # Введите строку: Кажется, я забыл выключить утюг
    # Результат: Кажется, Я Забыл Выключить Утюг
    user_text = input('Enter your message: ')
    print(user_text.title())


def ex19_6_5():
    # Задача 5. Пароль
    # При регистрации на сайте помимо логина нужно ещё придумать надёжный пароль. Этот пароль должен состоять минимум из
    # восьми символов, в нём должна быть хотя бы одна большая буква и хотя бы три цифры. Тогда он будет считаться надёжным.
    # Напишите программу, которая запрашивает у пользователя пароль до тех пор, пока он не введёт надежный пароль.
    # Используется латиница.
    #
    # Пример:
    # Придумайте пароль: qwerty
    # Пароль ненадёжный. Попробуйте ещё раз.
    #
    # Придумайте пароль: qwerty12
    # Пароль ненадёжный. Попробуйте ещё раз.
    #
    # Придумайте пароль: qwerty123
    # Пароль ненадёжный. Попробуйте ещё раз.
    #
    # Придумайте пароль: qWErty123
    # Это надёжный пароль!
    def is_password_correct(user_password):
        digits_count = 0
        has_capital = False
        for i_sym in range(len(user_password)):
            if user_password[i_sym].isdigit():
                digits_count += 1
            if user_password[i_sym].isupper():
                has_capital = True
        return has_capital and digits_count >= 3 and len(user_password) >= 8

    password = input('Enter your password: ')
    while not is_password_correct(password):
        password = input('Пароль ненадёжный. Попробуйте ещё раз: ')
    print('Это надёжный пароль!')


def ex19_6_6():
    # С увеличением объёма данных возникла потребность в сжатии этих данных, при этом без потери важной информации. Для
    # этого было придумано кодирование, которое осуществляется следующим образом:
    #
    # s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот
    # символ и количество его повторений в этой позиции строки.
    #
    # Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
    # последовательность на экран. Кодирование должно учитывать регистр символов.
    #
    # Пример:
    # Введите строку: aaAAbbсaaaA
    # Закодированная строка: a2A2b2с1a3A1
    user_message = input('Enter your msg: ')
    count_repeater = 1
    current_symbol = user_message[0]
    next_symbol = user_message[1]
    result_message = ''
    for i_sym in range(len(user_message) - 1):
        current_symbol = user_message[i_sym]
        next_symbol = user_message[i_sym + 1]
        if current_symbol == next_symbol:
            count_repeater += 1
        else:
            result_message += current_symbol + str(count_repeater)
            count_repeater = 1
    if user_message[len(user_message) - 1] == user_message[len(user_message) - 2]:
        count_repeater += 1
    else:
        result_message += user_message[len(user_message) - 1] + str(count_repeater)
        count_repeater = 1
    print(result_message)


def ex19_6_7():
    global ip_address
    # Задача 7. IP-адрес 2
    # При написании клиент-серверного приложения часто приходится работать с теми самыми IP-адресами. Как мы уже
    # знаем, IP-адрес состоит из четырёх целых чисел в диапазоне от 0 до 255, разделённых точками.
    # Пользователь вводит строку. Напишите программу, которая определяет, является ли заданная строка правильным
    # IP-адресом. Обеспечьте контроль ввода, где предусматривается ввод целых чисел от 0 до 255, а также точки между ними.
    #
    # Пример 1:
    # Введите IP: 128.16.35.a4
    # a4 - не целое число
    #
    # Пример 2:
    # Введите IP: 240.127.56.340
    # 340 превышает 255
    #
    # Пример 3:
    # Введите IP: 34.56.42,5
    # Адрес - это четыре числа, разделённые точками
    #
    # Пример 4:
    # Введите IP: 128.0.0.255
    # IP-адрес корректен
    ip_address = input('Enter IP-address: ').split(".")

    def is_ipaddress_ok():
        if len(ip_address) < 4:
            print('Вы ввели неправильный IP. Неверное количество частей')
            return False
        for i_part in range(len(ip_address)):
            if not ip_address[i_part].isdigit():
                print('{} - не целое число'.format(ip_address[i_part]))
                return False
            elif int(ip_address[i_part]) > 255:
                print('{} превышает 255'.format(ip_address[i_part]))
                return False
            elif int(ip_address[i_part]) < 0:
                print('{} меньше 0'.format(ip_address[i_part]))
                return False
        return True

    if is_ipaddress_ok():
        print('IP-адрес {} корректен'.format('.'.join(ip_address)))



