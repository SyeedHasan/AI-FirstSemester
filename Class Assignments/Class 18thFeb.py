# Name: Syed Hasan
# Question Number 1

import numpy as np

#Find dot product of vector
def dotProduct(listA, listB):
#    return sum([listA[i]*listB[i] for i in range(len(listA))])

    return sum([x*y for x,y in zip(listA,listB)])
    
#    listC = []
#    for i in range(len(listA)):
#        listC.append(listA[i]*listB[i])
#    
#    return sum(listC)
        
a = dotProduct([1,2,3], [1,4,5])
print(a)

def pythonFunc(n):
    
    a = range(n)
    #print(a )
    #print(list(a))
    b = range(n)
    c = []
    
    for i in range(len(a)):
        x = i**2;
        y = i**3;
        c.append(x+y)
        
    return c
   
def numpyFunc(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a+b
    d = np.dot(c,a)

#list1 = pythonFunc(10)
#print(list1)
#list2 = numpyFunc(10)
#print(list2)

