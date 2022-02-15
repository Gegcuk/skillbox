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


def ex25_3_2():
    # Задача 2. Семья
    #
    # Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:
    #
    # Отобразить информацию о себе.
    # Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
    # Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
    # Создайте как минимум один экземпляр класса и проверьте работу методов.
    #
    # Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
    #
    # Family name: Common family
    # Family funds: 100000
    # Having a house: False
    #
    # Try to buy a house
    # Not enough money!
    #
    # Earned 800000 money! Current value: 900000
    # Try to buy a house again
    # House purchased! Current money: 0.0
    #
    # Family name: Common family
    # Family funds: 0.0
    # Having a house: True
    class Family:
        name = 'Simpsons'
        funds = 100000
        with_home = False

        def info(self):
            print('Family name: {}\nFamily funds: {}\nHas house? {}'.format(self.name,
                                                                            self.funds,
                                                                            self.with_home))

        def earn_money(self, earned_money):
            self.funds += earned_money

        def buy_house(self, price, discount=0):
            price = price - price * discount / 100
            if price > self.funds:
                print('You cannot buy house.')
            else:
                print('You have house!')
                self.funds -= price
                self.with_home = True

    family_1 = Family()
    family_1.info()
    family_1.buy_house(200000)
    family_1.earn_money(101000)
    family_1.buy_house(200000, 10)
    family_1.info()
