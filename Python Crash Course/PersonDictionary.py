

#6-1
def personDict():
    person = {}
    
    person['firstName'] = "Syed"
    person['lastName'] = "Hasan"
    person['city'] = "Karachi"
    
    print(person)
    print(person['firstName'])
    print(person['lastName'])
    print(person['city'])

#6-2
    
def favNum():
    print("Too easy!")
    
#6-3
    
def glossaryDict():
    actualDict = {}
    
    actualDict['this'] = "This refers to the calling object"
    actualDict['library'] = "Set of system files"
    actualDict['Polymorphism'] = "Different"
    actualDict['Inheritance'] = "Inherit something"
    
    for k in actualDict:
        print(k, ":", actualDict[k], end=" \n")        
glossaryDict()