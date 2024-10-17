import AnimalShelter
import  Animal

#creating 3 Animal
animal = Animal.Animal("dog", 12.2, 3, "RUFFLE")
animal2 = Animal.Animal("dog", 4.2, 2, "TOMMY")
animal3 = Animal.Animal("bear", 114.2, 12, "Jym")

#creating the object of Animal Shelter
a = AnimalShelter.AnimalShelter()

#adding 3 animal
a.addAnimal(animal)
a.addAnimal(animal2)
a.addAnimal(animal3)
#getting all animal of type dog
print("Species of dog type")
print(a.getAnimalsBySpecies("dog"))
#getting all animal of type bear
print("Species of Bear Type")
print(a.getAnimalsBySpecies("bear"))

#check if bear still exist
print("Is bear animal exist:" , a.doesAnimalExist(animal3))
#remove bear
print("Removing Bear")
a.removeAnimal(animal3)
#check if bear still exist
print("Is bear animal exist:" , a.doesAnimalExist(animal3))

