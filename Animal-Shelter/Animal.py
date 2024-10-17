class Animal:
    ''' Animal class type that contains animal values '''
    def __init__(self, species=None, weight=None, age=None, name=None):
        if species == None:
            self.species = species
        else:
            self.species = species.upper()
        self.weight = weight
        self.age = age
        if name == None:
            self.name = name
        else:
            self.name = name.upper()

    def setSpecies(self, species):
        if species == None:
            self.species = species
        else:
            self.species = species.upper()
        
    def setWeight(self, weight):
        self.weight = weight
        
    def setAge(self, age):
        self.age = age
        
    def setName(self, name):
        if name == None:
            self.name = name
        else:
            self.name = name.upper()

    def toString(self):
        return "Species: "+str(self.species)+", Name: "+str(self.name)+", Age: "+str(self.age)+", Weight: "+str(self.weight)

        
