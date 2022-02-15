import random


def ex25_3_1():
    # Задача 1. Машина 2
    #
    # Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
    #
    # цвет машины (например, красный),
    # цена (один миллион),
    # максимальная скорость (200),
    # текущая скорость (ноль).
    #
    #
    # Добавьте два метода класса:
    #
    # Отображение информации об объекте класса.
    # Метод, который позволяет устанавливать текущую скорость машины.
    # Проверьте работу этих методов.
    class Toyota:
        color = 'red'
        price = 1000000
        max_speed = 200
        current_speed = 0

        def info(self):
            print('Color:{}\nPrice:{}\nMax speed:{}\nCurrent speed:{}\n'.format(self.color,
                                                                                self.price,
                                                                                self.max_speed,
                                                                                self.current_speed
                                                                                ))

        def set_speed(self, speed):
            self.current_speed = speed

    first_toyota = Toyota()
    second_toyota = Toyota()
    third_toyota = Toyota()
    first_toyota.set_speed(random.randint(0, 200))
    second_toyota.set_speed(random.randint(0, 200))
    third_toyota.set_speed(random.randint(0, 200))
    first_toyota.info()
    second_toyota.info()
    third_toyota.info()


