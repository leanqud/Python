from Pizza import Pizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        self.size = size
        self.name = name
        if self.size == 'S':
            self.price = 12.00
        elif self.size == 'M':
            self.price = 14.00
        elif self.size == 'L':
            self.price = 16.00

    def getPizzaDetails(self):
        return f"SPECIALTY PIZZA\n\
Size: {super().getSize()}\n\
Name: {self.name}\n\
Price: ${super().getPrice():.2f}\n"
