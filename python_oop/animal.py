class Animal:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def walk(self):
        self.health -=1
        return self
    def run(self):
        self.health -=5
        return self
    def displayHealth(self):
        print(str(self.name) + "\nHealth: " + str(self.health))
        return self
animal1=Animal("bubi",100)
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Kitty", 100)
dog1.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health = 170

    def fly(self):
        self.health -=10
        return self
    
    def dragonDisplay(self):
        super().displayHealth()
        print("i am a dragon")
        return self

dragon1 = Dragon("Hopper", 100)
dragon1.fly().fly().fly().dragonDisplay()

class Pig(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 250
    
    def oink(self):
        self.health += 10
        return self
    
    def displayPig(self):
         super().displayHealth()
         print("I am a piglet")
         return self        

pig_one = Pig("Hammerton", 100)
pig_one.oink().oink().oink().displayPig()