#encapsulation
#python public, private, protected variables

class myCapsule:
    def __init__(self):
        self.a = 10     #a = public
        self._b = 20    #b = partially private, but convention, can be accessed
        self.__c = 30   #c = private, restricted 


capsule1 = myCapsule()

print(capsule1.a)  #will print
print(capsule1._b)  #will print
print(capsule1.__c) #won't print




