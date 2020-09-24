class Farm:
    def __init__(self, name, farm={}):
        self.name = name
        self.farm = farm

    def add_animal(self, animal, number_animals=1):
        if animal in self.farm:
            self.farm[animal] += number_animals
        else:
            self.farm[animal] = number_animals

    def get_info(self):
        print(self.name, "Farm")
        for key, value in self.farm.items():
            print(f"{key} \t\t\t {value}")
        print('E-I-E-I-O')

    def get_animal_types(self):
        animals = list(self.farm.keys())
        animals.sort()
        return animals
