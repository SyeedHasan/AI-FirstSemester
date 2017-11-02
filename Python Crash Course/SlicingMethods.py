import math

myList = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Fandango']

print("The first three items in the list are:")
print(myList[0:3])
print("The last three items in the list are: ")
print(myList[-3:])
print("The three items in the middle of the list are: ")
length = len(myList)
length = math.floor(length/2 - 1)

print(myList[length:length+3])
