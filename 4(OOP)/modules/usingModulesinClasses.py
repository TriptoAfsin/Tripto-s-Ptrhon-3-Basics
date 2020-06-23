from customModules.myPolygon import Polygon

class Rectangle(Polygon):
    def are(self):
        return self.get_width() * self.get_height() #we can't use __width or __height

#sub class
class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() /2


myTriangle = Triangle()

myTriangle.set_values(5, 6)
print(myTriangle.area())