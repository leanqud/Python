from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.time = time
        self.pizza = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizza.append(pizza)

    def getOrderDescription(self):
        joining ="\n----\n" 
        return f"******\n\
Order Time: {self.getTime()}\n\
{joining.join([pizza.getPizzaDetails() for pizza in self.pizza])}\
\n\
----\n\
TOTAL ORDER PRICE: ${sum([(pizza.getPrice()) for pizza in self.pizza]):.2f}\n\
******\n"
              
