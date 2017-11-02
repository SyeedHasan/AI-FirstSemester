import math

def findOdd(num):
    for number in range(1, num):
        if (number % 2) != 0:
            print(number, end=" ")
    print()

        
def findPrime(num):
    print("Prime Numbers: ")
    
    for value in range(2, num+1):
        flag = 0
        for thisValue in range(2, value):
            if(value % thisValue == 0):
                flag=1
                break
        
        if flag==0:
            print(value)
       

def squareRootedPrimes(num):
    
    print("Prime Numbers using Square Rooted Method:  ")
    for currentNumber in range( 1 , num):
        flag = 0
        
        for thisNumber in range( 2 , int(math.sqrt(num))):
            
            if(currentNumber/thisNumber) == 0:
                flag = 1
                break
        
        if flag == 0:
            print("This is a prime number" + str(currentNumber))
        

#Test these using your own 'test methods'
    
        
        
    
