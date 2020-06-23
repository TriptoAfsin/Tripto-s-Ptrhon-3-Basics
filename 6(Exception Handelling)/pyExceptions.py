fh = open('I:\\PythonProjects 2020\\5(PyIO)\\sample.txt', 'a') #write mode(w): will overwrite everytime
                                #append mode(a): append the file
fh_read = open('I:\\PythonProjects 2020\\5(PyIO)\\sample.txt', 'r')

myArray = [1,2,3,4,5,6,7,8,9,10]

try:
    fh.write('\nHello from python code\n how are you_3')
    for i in range(0, 10):
        fh.write("\n %s" %myArray[i]) #writing from an array 

    print(fh_read.read()) #reading a txt file(whole)
    print(fh_read.readlines()[0:5]) #will read as list , but you've disable the first 
    

finally:
    fh.close() #good practise
