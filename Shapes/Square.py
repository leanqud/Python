from Shape2D import Shape2D

class Square(Shape2D):

    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        self.area = self.side ** 2
        return self.area

    def computePerimeter(self):
        self.perimeter = 4 * self.side
        return self.perimeter

    def getShapeProperties(self):
        return "Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}" \
               .strip().format(self.color, self.side, self.area, self.perimeter)
        
