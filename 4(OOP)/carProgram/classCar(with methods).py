counterObjects = 0

class Car:
   def __init__(self, speed, color):  #method, self: argument(automatically provided), init: class constructer , self is like "this" in java
       print("init is called") # it will be printed , as many of the objects present of that class 
       print("Speed: ",  speed)
       print("Color: ", color)
       self.speed = speed  #else ford.speed can't be done 
       self.Color = color






#creating instance of a class 

ford = Car(200, "Red")  #ford is a object / instance of car class
toyota = Car(150, "White") 
audi = Car(250, "Ash")
BMW = Car(250, "Blue")

print(ford.speed)



