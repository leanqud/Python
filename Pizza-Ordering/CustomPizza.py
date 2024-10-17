from Pizza import Pizza

class CustomPizza(Pizza):
  def __init__(self,size):
    super().__init__(size)
    self.toppings =[]
    if size == "S":
      super().setPrice(8.00)
    elif size == "M":
      super().setPrice(10.00)
    elif size == "L":
      super().setPrice(12.00)

  def addTopping(self,topping):
    self.toppings.append(topping)
    if self.size == "S":
      super().setPrice(self.getPrice()+0.5)
    elif self.size == "M":
      super().setPrice(self.getPrice()+0.75)
    elif self.size == "L":
      super().setPrice(self.getPrice()+1)   

  def getPizzaDetails(self):
    newTopping = "\n\t+ "
    tab = '\t+ '
    newline ='\n'
    return f"CUSTOM PIZZA\nSize: {self.getSize()}\nToppings:{newline+tab+newTopping.join(self.toppings)  if len(self.toppings)>0 else ''}\nPrice: ${super().getPrice():.2f}\n" 
