class Human:
    def __init__(self):
        self.health = 5
        self.intelligence = 3
        self.strength = 2
        self.stealth = 1 
class Wizard(Human):
    def __init__(self):
        super().__init__()
        self.intelligence=10
    def heal(self):
        self.health +=10
class Ninja(Human):
    def __init__(self):
        super().__init__()
        self.stealth =10
    def steal(self):
        self.stealth+=5
class Samurai(Human): 
    def __init__(self):
        super().__init__()
        self.strength=10
    def sacrifice(self):
        self.health-=5