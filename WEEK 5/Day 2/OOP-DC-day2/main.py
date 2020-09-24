import random
class Gene():
    def __init__(self):
        self.value = random.choice([True, False])
    
    def mutate(self):
        self.value = not self.value

class Chromosome():
    def __init__(self):
        self.value = 
        
class DNA():
    def __init__(self, chromosomes ='', genes ='' ):
        self.chromosomes = chromosomes
        self.genes = genes


    

def main():
    dna = DNA()
    print(chromosome)
    print(genes)
    print([random.randint(0,1)]*10)


if __name__ == "__main__":
    main()