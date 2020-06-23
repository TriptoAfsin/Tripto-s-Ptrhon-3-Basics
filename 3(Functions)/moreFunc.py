#setting default values to arguments 
def myFunc(arg1 = 1, arg2 = 1):
    area = arg1*arg2
    return area

#variable length, best practise: use this arg at last
def marksFunc(name, age, *marks):
    print("Name: %s" %name)
    print("Age: %s" %age)
    print("Marks: ", marks)




def marksFuncDetailed(name, age, **marks):  # double * means they are keys
    print("Name: %s" %name)
    print("Age: %s" %age)
    print("Marks: ", marks)    


print(myFunc(5)) # will print, 5 x1 = 5   



x = int(input("Enter lenghth: "))
y = int(input("Enter width: "))

print("Area: %d" %myFunc(x,y))



marksFunc("Tripto", 22, 90,80,85) # when using * we don't know how many arguments we can put , marks is now tuple 

marksFuncDetailed("Tripto", 22, eng = 90, bangla = 80, math = 85) #marks is now dictionary
    
