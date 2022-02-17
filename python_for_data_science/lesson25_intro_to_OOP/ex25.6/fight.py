class Warrior:
    health = 100
    index = 1


    def __init__(self, health = 100):
        self.health = health
        self.index = Warrior.index
        Warrior.index += 1

    def punch(self, warrior, damage = 20):
        warrior.health -= damage
        warrior.info()

    def info(self):
        print('Warrior {} has {} health'.format(self.index, self.health))
