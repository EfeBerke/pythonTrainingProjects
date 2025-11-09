class Zoo():
    def __init__(self):
        self._animals = []

    def AddAnimal(self, animal):
        self._animals.append(animal)

    def Print(self):
        num_of_birds = [0]
        num_of_mammals = [0]
        sound_of_animals = []
        for an in self._animals:
            an.CollectSounds(sound_of_animals)
            an.MammalCount(num_of_mammals)
            an.BirdCount(num_of_birds)
            
        print(f"This zoo has {num_of_mammals[0]} mammals and {num_of_birds[0]} birds. The sounds of the animals are: {' '.join(sound_of_animals)}")


class Animal():
    def __init__(self, sound=None):
        self._sound = sound

    # Polymorphism
    def MammalCount(self, counter): 
        pass

    def BirdCount(self, counter):
        pass

    def CollectSounds(self, sound_list):
        sound_list.append(self._sound)


class Lion(Animal):
    def __init__(self):
        super().__init__(sound = "Roar")

    def MammalCount(self, counter):
        counter[0] += 1

class Cat(Animal):
    def __init__(self):
        super().__init__(sound = "Meow")
    
    def MammalCount(self, counter):
        counter[0] += 1

class Sparrow(Animal):
    def __init__(self):
        super().__init__(sound = "Chirp")

    def BirdCount(self, counter):
        counter[0] += 1

def Run():
    zoo = Zoo()
    lion = Lion()
    cat = Cat()
    sparrow = Sparrow()
    zoo.AddAnimal(lion)
    zoo.AddAnimal(cat)
    zoo.AddAnimal(sparrow)
    zoo.Print()

Run()
