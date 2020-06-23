x = int(input("Enter X: "))
y = int(input("Enter Y: "))

if x > y:
    print("X is Bigger") #no indentation no if stuff

if x == y:
    print("They are same")

else:
    print("Y is bigger")  


print("Weird syntax tbh")   

#else if  = elif 

if x > y:
    print("X is Bigger") #no indentation no if stuff

elif x == y:
    print("They are same")
    if x%2 == 0:
        print("And they are also even")
    else:
         print("And they are also odd")   

else:
    print("Y is bigger")  