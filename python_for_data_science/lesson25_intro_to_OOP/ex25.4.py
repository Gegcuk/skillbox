def ex25_4_1():
    # Задача 1. Машина 3
    #
    # Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
    #
    # Четыре атрибута:
    #
    # цвет машины (например, красный),
    # цена (один миллион),
    # максимальная скорость (200),
    # текущая скорость (ноль).
    # Два метода:
    #
    # Отображение информации об объекте класса.
    # Метод, который позволяет устанавливать текущую скорость машины.
    # Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
    class Toyota:
        color = 'red'
        price = 1000000
        max_speed = 200
        current_speed = 0

        def __init__(self, color='red', price=1000000, max_speed=200, current_speed=0):
            self.current_speed = current_speed
            self.price = price
            self.color = color
            self.max_speed = max_speed

        def info(self):
            print('Color:{}\nPrice:{}\nMax speed:{}\nCurrent speed:{}\n'.format(self.color,
                                                                                self.price,
                                                                                self.max_speed,
                                                                                self.current_speed
                                                                                ))

        def set_speed(self, speed):
            self.current_speed = speed

    car_1 = Toyota()
    car_2 = Toyota('blue', 20000, 250)
    car_1.info()
    car_2.info()


