class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
        self.backpack = []

    def eat (self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')

    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')

    def change_alias(self, new_alias):
        print(self)
        self.alias = new_alias

    def beat_up(self, foe):
        if not isinstance (foe, Character):
            return
        if foe.power < self.power:
            foe.status = 'defeated'
            self.status = 'winner'
        else:
            print('Retreat!')

bruce = Character('Bruce wayne', 85)
peter = Character('Peter Parker', 80)

bruce.beat_up(peter)
peter.beat_up(bruce)

print(peter.status) 
print(bruce.status) 