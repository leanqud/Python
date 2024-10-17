from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0

    def addCar(self, car):
        if self.root:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)
        self.size += 1

    def _addCar(self, car, currentNode):
        temporaryNode = CarInventoryNode(car)
        if temporaryNode == currentNode:
            currentNode.cars.append(car)
        elif temporaryNode < currentNode:
            if currentNode.left:
                self._addCar(car, currentNode.left)
            else:
                currentNode.left = temporaryNode
                temporaryNode.parent = currentNode
        elif temporaryNode > currentNode:
            if currentNode.right:
                self._addCar(car, currentNode.right)
            else:
                currentNode.right = temporaryNode
                temporaryNode.parent = currentNode
        else:
            currentNode.count += 1

    def doesCarExist(self, car): #3
        if self.root:
            ex = self._get(car, self.root)
            if ex:
                for i in ex.cars:
                    if i == car:
                        return True
        return False

    def _get(self, car, currentNode):
        temporaryNode = CarInventoryNode(car)
        if not currentNode:
            return None
        elif temporaryNode == currentNode:
            return currentNode
        elif temporaryNode < currentNode:
            return self._get(car, currentNode.getLeft())
        else:
            return self._get(car, currentNode.getRight())
        
    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, node):
        ex = ""
        if node:
            ex += self._inOrder(node.getLeft())
            ex += str(node)
            ex += self._inOrder(node.getRight())
        return ex

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, node):
        ex = ""
        if node:
            ex += str(node)
            ex += self._preOrder(node.getLeft())
            ex += self._preOrder(node.getRight())
        return ex

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, node):
        ex = ""
        if node:
            ex += self._inOrder(node.getLeft())
            ex += self._inOrder(node.getRight())
            ex += str(node)
        return ex

    def getBestCar(self, make, model): #4
        tempCar = Car(make, model, 0, 0)
        if self.root:
            ex = self._get(tempCar, self.root)
            if ex:
                if len(ex.cars) == 1:
                    return ex.cars[0]
                else:
                    best = ex.cars[0]
                    for i in ex.cars:
                        if i > best:
                            best = i
                    return best
        return None

    def getWorstCar(self, make, model): #5
        tempCar = Car(make, model, 0, 0)
        if self.root:
            ex = self._get(tempCar, self.root)
            if ex:
                if len(ex.cars) == 1:
                    return ex.cars[0]
                else:
                    worst = ex.cars[0]
                    for i in ex.cars:
                        if i < worst:
                            worst = i
                    return worst
        return None

    def _ipHelper(self, node):
        totalPrice = 0
        if node:
            totalPrice += self._ipHelper(node.getLeft())
            for i in node.cars:
                totalPrice = totalPrice + i.price
            totalPrice += self._ipHelper(node.getRight())
        return totalPrice

    def getTotalInventoryPrice(self): #6
        return self._ipHelper(self.root)

    def getSuccessor(self, make, model):
        tempCar = Car(make, model, 0, 0)
        if self.root:
            output = self._get(tempCar, self.root)
            if output:
                if output.getRight():
                    output = output.getRight()
                    while output.getLeft():
                        output = output.getLeft()
                    return output
                else:
                    ret = output
                    while output:
                        if output > ret:
                            return output
                        output = output.getParent()
        return None

    def _removeCar(self, node):
        if not node.getLeft() and not node.getRight():
            if node.parent.getLeft():
                if node == node.parent.getLeft():
                    node.parent.left = None
            if node.parent.getRight():
                if node == node.parent.getRight():
                    node.parent.right = None
        elif node.getLeft() and node.getRight():
            successor = self.getSuccessor(node.make, node.model)
            node.model = successor.model
            node.make = successor.make
        else:
            if node.getLeft():
                if not node.getParent():
                    node.left.parent = None
                    self.root = node.getLeft()
                else:
                    if node.getParent().getLeft():
                        if node.getParent().getLeft() == node:
                            node.left.parent = node.parent
                            node.parent.left = node.left
                        if node.getParent().getRight():
                            if node.getParent().getRight() == node:
                                node.left.parent = node.parent
                                node.parent.right = node.left
            else:
                if not node.getParent():
                    node.right.parent = None
                    self.root = node.right
                else:
                    if node.getParent().getLeft():
                        if node.getParent().getLeft() == node:
                            node.right.parent = node.parent
                            node.parent.left = node.right
                        if node.getParent().getRight():
                            if node.getParent().getRight() == node:
                                node.right.parent = node.parent
                                node.parent.right = node.right
    
    def removeCar(self, make, model, year, price):
        tempCar = Car(make, model, year, price)
        removal = self._get(tempCar, self.root)
        if removal:
            self._removeCar(removal)
            self.size = self.size - 1
            return True
        else:
            return False
        helpme = self.doesCarExist(self, tempCar)
        if helpme:
            self._removeCar(helpme)
            if self.size > 0:
                return True
        else:
            return False
        if self.size > 1:
            removal = self._get(tempCar, self.root)
            if removal:
                self._removeCar(removal)
                self.size = self.size - 1
                return True
            else:
                return False
        if self.size == 1 and self.node == self.root:
            self.root = None
            self.size = self.size - 1
            return True
        else:
            return False
