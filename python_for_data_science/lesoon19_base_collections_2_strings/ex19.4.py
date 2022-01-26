def ex19_4_1():
    # Задача 1. Шифр Цезаря 2
    #
    # Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком способе шифрования
    # каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
    #
    # Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и
    # сделайте так, чтобы текст был в одном регистре.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = int(input("Enter shift for code: "))
    word_for_encrypt = str(input("Enter the word for encrypt: ").lower())
    new_word = [(alphabet[(alphabet.index(sym) + shift) % 26] if sym != " " else " ") for sym in word_for_encrypt]
    print(''.join(new_word))


def ex19_4_2():
    # Задача 2. Путь к файлу
    # Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта часто используются абсолютные пути
    # файлов, которые необходимо проверять.
    #
    # Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные: диск и расширение файла.
    # Напишите программу, которая проверяет корректность этого пути.
    #
    # Пример:
    # Путь к файлу: C:/user/docs/folder/new_file.txt
    # На каком диске должен лежать файл: C
    # Требуемое расширение файла: .txt
    # Путь корректен!
    full_path = input("Enter the full path to file: ")
    file_disc = input("Enter disc: ")
    file_ext = input("Enter file extension: ")
    if full_path.startswith(file_disc) and full_path.endswith(file_ext):
        print("Path is correct!")
    else:
        print("You entered wrong path.")


def ex19_4_3():
    # Задача 3. Удаление части
    # На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы. Напишите код, который
    # проверяет, каких букв в строке больше, прописных или заглавных. Если заглавных букв больше, то сделать все буквы
    # строки заглавными, иначе сделать все прописными.
    #
    # Подсказка: используйте методы islower() и/или isupper().
    #
    # Пример:
    # Введите строку: ПитоН - этО хорошО
    # Результат: питон - это хорошо
    #
    # Пример 2:
    # Введите строку: ПиТоН - ЭтО УДоБнО
    # Результат: ПИТОН - ЭТО УДОБНО

    user_string = input("Enter your msg: ")
    count_lower = 0
    count_upper = 0
    for i_sym in range(len(user_string)):
        if user_string[i_sym].islower():
            count_lower += 1
        else:
            count_upper += 1
    if count_lower >= count_upper:
        print(user_string.lower())
    else:
        print(user_string.upper())

