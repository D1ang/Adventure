class Beast:

    # Dunder method ~ The __init__ will create this when requested
    def __init__(self, health, mana, speed):
        self.health = health
        self.mana = mana
        self.speed = speed

    # methods
    def attack(self, amount):
        print('The beast attacked!')
        print(f'{amount} damage was dealt')
        self.mana -= 10
    
    def move(self, amount):
        print('The beast moved forward')
        print(f'it moved with a speed of {amount} miles')
        self.speed -= 1
        print(f'The beast has {self.speed} moves left')


beast1 = Beast(health=100, mana=50, speed=20)
beast2 = Beast(50, 100, 5)


print(beast1.health)
print(beast2.health)
