from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException
import pytest

def test_Pizza():
    p1 = Pizza('S')
    p1.setPrice(8.00)
    p1.setSize('S')
    assert p1.getPrice() == 8.00
    assert p1.getSize() == 'S'

def test_CustomPizza1():
    cp1 = CustomPizza("S")
    print(cp1.getPizzaDetails())
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"

def test_CustomPizza2():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"

def test_getPizzaDetails():
    sp1 = SpecialtyPizza("S", "Carne-more")
    print(sp1.getPizzaDetails())
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"

def test_getOrderDescription():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test_QueueEmptyException():
    with pytest.raises(QueueEmptyException):
        heap = OrderQueue()
        heap.processNextOrder()
