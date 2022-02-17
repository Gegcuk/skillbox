from fight import Warrior

warrior_1 = Warrior(200)
warrior_2 = Warrior(300)

warrior_1.punch(warrior_2)
warrior_2.punch(warrior_1)
warrior_2.punch(warrior_1)
warrior_2.punch(warrior_1)
warrior_1.punch(warrior_2)