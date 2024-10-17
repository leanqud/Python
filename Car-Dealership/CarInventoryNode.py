from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        ret = ''
        for i in self.cars:
            ret += str(i) + '\n'
        return ret

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
        return False  

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
        return False

    def __eq__(self, rhs):
        if rhs == None:
            return False
        elif self.make == rhs.make:
            if self.model == rhs.model:
                return True
        return False

