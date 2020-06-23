class Car:
    pass  #pass: empty class/ method



#creating instance of a class 

ford = Car()  #ford is a object / instance of car class
toyota = Car() 
audi = Car()
BMW = Car()

ford.speed = 200  #speed,color is an attribute 
ford.color = "Red"
print("Ford: \n  Speed: %d" %ford.speed)
print("  Color: %s" %ford.color)


toyota.speed = 150
toyota.color = "White"
print("Toyota: \n  Speed: %d" %toyota.speed)
print("  Color: %s" %toyota.color)


audi.speed = 220
audi.color = "Ash"
print("Audi: \n  Speed: %d" %audi.speed)
print("  Color: %s" %audi.color)

BMW.speed = 200
BMW.color = "Blue"
print("BMW: \n  Speed: %d" %BMW.speed)
print("  Color: %s" %BMW.color)
