#super class 

class Parent:
    def __init__(self, name):
        print("I'm the parent of ", name )


class child(Parent):
    def __init__(self):
        print("I'm the child of my parent")
        super().__init__("Tripto") #using super 


child1 = child()
print(child.__mro__) #parent resolution order 