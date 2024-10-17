from Shape2D import Shape2D
from Circle import Circle
from Square import Square

def test_Shape2D():
    s1 = Shape2D("blue")
    assert s1.getColor() == "blue"
    assert s1.getShapeProperties() == "Shape: N/A, Color: blue"

def test_Circle():
    c1 = Circle("blue", 2.5)
    assert c1.getRadius() == 2.5
    assert c1.computeArea() == 19.6349375
    assert c1.computePerimeter() == 15.70795
    assert c1.getShapeProperties() == "Shape: CIRCLE, Color: blue, Radius: 2.5, Area: 19.6349375, Perimeter: 15.70795"

def test_Square():
    s1 = Square("blue", 2.5)
    assert s1.getSide() == 2.5
    assert s1.computeArea() == 6.25
    assert s1.computePerimeter() == 10.0
    assert s1.getShapeProperties() == "Shape: SQUARE, Color: blue, Side: 2.5, Area: 6.25, Perimeter: 10.0"
