class Zoo():
    def __init__(self):
        self._cages = []

    def add_cage(self, cage):
        self._cages.append(cage)

    def open_show(self):
        for cage in self._cages:
            for animal in cage.get_animal_list():
                animal.sound_of_animal()

class Cage():
    def __init__(self):
        self._animals = []
    
    def add_animal(self, animal):
        self._animals.append(animal)

    # Public Function
    def get_animal_list(self):
        return self._animals


class Animal():
    def __init__(self, name):
        self._name = name

    # Polymorphism
    def sound_of_animal(self): 
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound_of_animal(self):
        print("Roar")

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound_of_animal(self):
        print("Trumpet")


zoo = Zoo()

c1 = Cage()
c2 = Cage()

c1.add_animal(Lion("Simba"))
c1.add_animal(Elephant("Dumbo"))

c2.add_animal(Lion("Mufasa"))

zoo.add_cage(c1)
zoo.add_cage(c2)

zoo.open_show()

