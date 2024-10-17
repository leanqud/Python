from Animal import Animal

class AnimalShelter:

    def __init__(self):
        self.animalshelter = {}

    def addAnimal(self, animal):
        if animal.species in self.animalshelter:
            self.animalshelter[animal.species].append(animal)
        else:
            self.animalshelter[animal.species] = [animal]
    
    def removeAnimal(self,animal):
        if animal.species in self.animalshelter:
            self.animalshelter[animal.species].remove(animal)
    
    def removeSpecies(self, species):
        species = species.upper()
        if species in self.animalshelter:
            self.animalshelter[species].remove(species)
    
    def getAnimalsBySpecies(self, species):
        species = species.upper()
        species_string = ""
        if species in self.animalshelter:
            for i in range(len(self.animalshelter[species])):
                if i < len(self.animalshelter[species]):
                    species_string = species_string + self.animalshelter[species][i].toString() + '\n'
                else:
                    species_string = species_string + self.animalshelter[species][i].toString().rstrip()
        return species_string
    
    def doesAnimalExist(self, animal):
        for i in self.animalshelter.keys():
            if animal in self.animalshelter[i]:
                return True
        return False

