from garden import PotatoGarden

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


def ex25_4_2():
    global Point

    # Задача 2. Координаты точки
    #
    # Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут передаваться пользовательские
    # значения координат, по умолчанию x = 0, y = 0.
    #
    # Реализуйте класс, который будет представлять эту точку, и напишите метод, который предоставляет информацию о ней.
    # Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.
    #
    # Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.
    class Point:
        x = 0
        y = 0
        counter = 0

        def __init__(self, x, y):
            self.y = y
            self.x = x
            Point.counter += 1

        def info(self):
            print('X: {} Y: {} Count: {}'.format(self.x, self.y, Point.counter))

    point_1 = Point(10, 20)
    point_2 = Point(10, 20)
    point_3 = Point(10, 20)
    point_4 = Point(10, 20)
    point_5 = Point(10, 20)
    point_6 = Point(10, 20)
    point_7 = Point(10, 20)
    point_8 = Point(10, 20)
    point_8.info()


my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
my_garden.grow_all()
my_garden.grow_all()
my_garden.grow_all()
my_garden.grow_all()
my_garden.are_all_ripe()