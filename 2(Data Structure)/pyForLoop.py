counter = 0
counterA = 0

usrName = str(input("Enter Your Name: "))

formatedName = usrName.lower()


for a in usrName:
    counter += 1 #will get the string length

print("Length: %d" %counter)   

for i in range(0, len(formatedName)): #have to use this range  0 to length of name
    if formatedName[i] == 'a':
        counterA += 1


print("Number of A: %d" %counterA)


for i in range(0,10):
    print(i)  #will print 0 to 9

for i in range(0,10):
    if i == 6:
        break
    else:
        print(i)


for i in range(0,10):
    if i == 6:
        continue # 6 will be skipped
    else:
        print(i)        