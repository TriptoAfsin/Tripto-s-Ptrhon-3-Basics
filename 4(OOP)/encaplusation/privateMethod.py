#encapsulation
#python public, private, protected variables

class myCapsule:
    def __init__(self):
        self.a = 10     #a = public
        self._b = 20    #b = partially private, but convention, can be accessed
        self.__c = 30   #c = private, restricted 
    def public_method(self):
        print(self.__c)
        print("Hi from public method")
        self.__private_method() #now you can access

    def __private_method(self):
        print("Hello from private method")  #can't be used outside the class 





capsule1 = myCapsule()

print(capsule1.a)  #will print
print(capsule1._b)  #will print
#print(capsule1.__c) #won't print

capsule1.public_method() # now c can be printed