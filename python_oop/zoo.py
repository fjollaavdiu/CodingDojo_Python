class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def addDog(self, name):
        self.animals.append(name)
    def addDragon(self, name):
        self.animals.append(name)
    def printAllHealth(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.displayHealth()
        return self
zoo1 = Zoo("John's Zoo")
zoo1.addDog("Tracy")
zoo1.addDog("Doggy")
zoo1.addDragon("Draggy")
zoo1.addDragon("Dragoon")
zoo1.printAllHealth()
