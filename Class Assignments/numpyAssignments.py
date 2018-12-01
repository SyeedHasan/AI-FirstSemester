import numpy as np

#Create an empty array
arr = np.array([])

a = np.arange(1,6)
#print(a)
b = np.arange(0,5)
#print(b)
#print(type(b))
#print(b.dtype)  #
#print(len(b)) #Shows the number of elements
#print (b.shape) #Shows number of rows/columns

#Creating a 2-D Array
twoD = np.array([np.arange(3), np.arange(3)])
#print(twoD)

#Creating another 2D Array
another2D = np.array([np.arange(3), np.arange(3), np.arange(3)])
print(another2D)
#print(another2D*3)
print(another2D.shape)
#print(another2D[1])

#We can also define the data type of our elements in our array
anotherArray = np.array([np.arange(4, dtype="float32"), np.arange(4)])
print(anotherArray)
