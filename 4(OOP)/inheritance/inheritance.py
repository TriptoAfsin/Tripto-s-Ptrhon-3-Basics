#takes inheritance from a base class 
# borrows behaviours from a base class
#superclass -> base class
#subclass -> child class 

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

#sub class
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