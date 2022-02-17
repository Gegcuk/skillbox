class Potato:
    states = {0: 'Planted', 1: 'Sprout', 2: 'Green', 3: 'Ripe'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state <3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Potato {} is {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range (1, count+1)]

    def grow_all(self):
        print('Potato is growing!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Potato is not ready')
        else:
            print('All potatoes are grown!')