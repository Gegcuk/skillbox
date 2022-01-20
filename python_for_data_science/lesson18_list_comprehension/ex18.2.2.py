# Задача 2. Сообщение
#
# Илья решил безобидно подшутить над другом и написал программу для смартфона, которая при отправке сообщения удваивает каждый символ строки и заодно к каждому удвоенному добавляет ещё один дополнительный.
#
# Пользователь вводит строку и дополнительный символ. Напишите программу, которая генерирует два списка: в первом списке каждый элемент — удвоенная буква первой строки, во втором списке каждый элемент — конкатенация элемента первого списка и дополнительного символа.
#
#
#
# Пример:
#
# Введите строку: привет
#
# Введите дополнительный символ: !
#
#
#
# Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']
#
# Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']

def get_doubled_list(message):
    return [message[i_sym] * 2 for i_sym in range(0, len(message))]


def get_doubled_letters_with_symbol_list(message, symbol):
    return [message[i_sym] * 2 + symbol for i_sym in range(0, len(message))]


message = input("Enter your message: ")
symbol = input("Enter your symbol:")

double_letters_message = get_doubled_list(message)
double_letters_with_symbol_message = get_doubled_letters_with_symbol_list(message, symbol)

print(double_letters_message)
print(double_letters_with_symbol_message)