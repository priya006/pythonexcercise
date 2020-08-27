from Inheritance.Polygon import Polygon

# Triangle is the Derived class of Polygon
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle() # Creating object for Triangle class
t.inputSides()
t.dispSides()

print(t.findArea())
