from abc import ABC, abstractmethod #importing abstract method 

#Parenet Class
class Shape(ABC):
    @abstractmethod #Now a abstract method, can't be instatnciated
    def area(self): #Empty Method
        pass

    @abstractmethod  #Now a abstract method, can't be instatnciated
    def perimeter(self):
        pass


#Child Class
class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self): # we have to do this to access the abstract class 
        return self.__side * self.__side

    def perimeter(self): # we have to do this to access the abstract class 
        return self.__side * 4       

myShape = Square(5)
print(myShape.area())
print(myShape.perimeter())
