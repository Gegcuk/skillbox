import random


def ex25_2_1():
    # Задача 1. Машина
    #
    # Напишите класс Toyota, состоящий из четырёх статических атрибутов:
    #
    # цвет машины (например, красный),
    # цена (один миллион),
    # максимальная скорость (200),
    # текущая скорость (ноль).
    # Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
    class Toyota:
        color = 'red'
        price = 100000
        max_speed = 200
        current_speed = 0

    first_toyota = Toyota()
    second_toyota = Toyota()
    third_toyota = Toyota()
    first_toyota.current_speed = random.randint(0, 200)
    second_toyota.current_speed = random.randint(0, 200)
    third_toyota.current_speed = random.randint(0, 200)
    print('1st toyota speed: {}\n2nd toyota speed: {}\n3rd toyota speed: {}'.format(first_toyota.current_speed,
                                                                                    second_toyota.current_speed,
                                                                                    third_toyota.current_speed))


def ex25_2_2():
    class Monitor:
        manufacturer = 'Samsung'
        matrix = 'VA'
        resolution = 'WQHD'
        frequency = 60

    class Headphones:
        manufacturer = 'Sony'
        sensitivity = 108
        with_microphone = False

    monitor_1 = Monitor()
    monitor_2 = Monitor()
    monitor_3 = Monitor()
    monitor_4 = Monitor()

    monitor_2.frequency = 144
    monitor_3.frequency = 70

    headphones_1 = Headphones()
    headphones_2 = Headphones()
    headphones_3 = Headphones()

    headphones_2.with_microphone = True
    headphones_3.with_microphone = True
