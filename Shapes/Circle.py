from Shape2D import Shape2D

class Circle(Shape2D):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def computeArea(self):
        self.area = 3.14159 * (self.radius ** 2)
        return self.area

    def computePerimeter(self):
        self.perimeter = 2 * 3.14159 * self.radius
        return self.perimeter

    def getShapeProperties(self):
        return "Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}" \
               .strip().format(self.color, self.radius, self.area, self.perimeter)

    
