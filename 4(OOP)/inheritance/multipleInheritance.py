# super class - 
class Polygon:
    __width = None  #private, won't be accisable by the sub classes 
    __height = None #private

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Shape:
    __color = None

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class Triangle(Polygon, Shape):  #multiple inheritance
    def area(self):
        return self.get_width() *self.get_height() / 2


myTriangle = Triangle()

myTriangle.set_color("Green")
print(myTriangle.get_color())


