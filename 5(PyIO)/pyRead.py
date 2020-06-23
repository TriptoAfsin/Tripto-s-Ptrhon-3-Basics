fh = open('I:\\PythonProjects 2020\\5(PyIO)\\sample_read.txt', 'r') 
print(fh) #will print the reading type

#reading every line 

#for i in fh:
    #print(i)

#checking the character of everyline
#j = 1
#totalCharac = 0

#for line in fh:
    #print("line {0} : {1}".format(j, len(line)))
    #totalCharac += len(line)
    #j += 1


#print("Total Charcter: {0}".format(totalCharac))


#checking total words eveyline

lineCounter = 1
totalWord = 0

for words in fh:
    print("line {0} : {1} words".format(lineCounter, len(words.split(" "))))
    totalWord += len(words.split(" "))
    lineCounter += 1


print("Total Word: {0}".format(totalWord))

fh.close()