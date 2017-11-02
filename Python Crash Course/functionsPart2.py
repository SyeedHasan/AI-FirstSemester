
#8-7

def Album(artistName, albumTitle, tracks=""):
    
    artistDict = {'name': artistName ,
                   'title': albumTitle
                 }
    
    if tracks:
        artistDict['noOfTracks'] = tracks
    
    return artistDict
    
#print(Album("Syed", "JMeero"))
#print(Album("Raseed", "Milo", 22))
#print(Album("Aseed", "Jemsro"))
    

#8-10

def showMagicians(names):
    for name in names:
        print(name)

def greatMagicians(names):
    changedNames = []
    while names:
        name = names.pop()
        name = "the Great " + name
        changedNames.append(name)
    
    return changedNames
    
#list = ['Abra', 'Dabra', 'Cobra', 'Salma']
#editedList = greatMagicians(list)
#showMagicians(editedList)
    
#8-12
    
def items(*allItems):
    print("Items: ")
    for item in allItems:
        print("\t-" + item)
        
#items('Pepper', 'Salt', 'Tomato')

#8-13
        
def build_profile(first, last, **user_info):
    profile = {}
    
    profile['first_name'] = first
    
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Syed', 'Hasan',
                             Fav_place='KFC' , 
                             Fav_food='Cheese',
                             Hobby='ABC')

#print(user_profile)

#8-14

def storeCar(manufacturer, modelNum, **otherStuff):
    
    otherStuff['Manufacturer'] = manufacturer
    otherStuff['Model Number'] = modelNum
    
    return otherStuff
    
    
myCar = storeCar('Subaru', 'Outback', color='Black', plate='AB21C', towNum='223B', seats='5')

print(myCar)    
    

