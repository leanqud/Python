from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car():
    c = Car("Honda", "CRV", 2007, 8000)
    assert print(c) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"

def test_CarInventoryNode():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    print(carNode)

def test_Getters():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    assert carNode.getMake() == 'DODGE'
    assert carNode.getModel() == 'DART'
    assert carNode.getParent() == None
    assert carNode.getLeft() == None
    assert carNode.getRight() == None

def test_CarInventory():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Mercedes", "Fish", 2022, 40000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.doesCarExist(car5) == True
    assert bst.doesCarExist(car6) == False

def test_Traversal():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Mercedes", "Fish", 2022, 40000)

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

    print(bst.getTotalInventoryPrice())
    assert bst.getTotalInventoryPrice() == 158000   

def test_inOrder():
    bst = CarInventory()
    
    assert bst.inOrder() == \
    "Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"


def test_preOrder():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Mercedes", "Fish", 2022, 40000)
    
    assert bst.preOrder() == \
    "Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
    
def test_postOrder():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Mercedes", "Fish", 2022, 40000)
    
    assert bst.postOrder() == \
    "Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n"

def test_ioTraversal():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.inOrder() == \
    "Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"

    bst.removeCar("BMW", "X5", 2022, 60000)

    assert bst.inOrder() == \
    "Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"

def test_proTraversal():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.preOrder() == \
    "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"

    bst.removeCar("BMW", "X5", 2022, 60000)

    assert bst.preOrder() == \
    "Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"

def test_postTraversal():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    print(bst)
    bst.removeCar("BMW", "X5", 2020, 58000)
    print(bst.removeCar("BMW", "X5", 2020, 58000))

    assert bst.postOrder() == \
    "Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"

    bst.removeCar("BMW", "X5", 2022, 60000)

    assert bst.preOrder() == \
    "Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n"

def test_getSuccessor():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getSuccessor(car5) == None
    assert bst.getSuccessor(car1) == \
    "Make: AUDI, Model: A3, Year: 2021, Price: $25000\n"
    
