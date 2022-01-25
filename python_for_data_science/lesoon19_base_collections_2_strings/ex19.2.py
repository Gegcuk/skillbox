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
