
#AdvancedDictionaries

#6-7
def personDict():
    person = {}
    person1 = {'favFood': 'Biryani'}
    person2 = {'favEatery':'KFC'}
    
    allPersons = [person, person1, person2]
    
    person['firstName'] = "Syed"
    person['lastName'] = "Hasan"
    person['city'] = "Karachi"
    
    for man in allPersons:
        print(man)
        

#6-8
def pets():
    dog = { 
            'type': 'Labrador',
            'owner': 'James'   
          }
    
    dog2 = {
               'type':'German',
               'owner': 'Mijo'
           }
    
    dog3 = {
                'type': 'Shepherd',
                'owner': 'Jawmal'
           }
    
    pets = [dog, dog2, dog3]
    
    for pet in pets:
        print(pet)
    

#6-9
def favPlaces():
    
    favoritePlaces = {
                
            'Syed': ["Karachi", "Lahore", "Peshawar"],
            'Jamal': ["K", "A", "B"],
            'Saweed': ["A", "B", "C"]
            
            }
    
    for name, places in favoritePlaces.items():
        print(name, end=":")
        for onePlace in places:
            print(onePlace, sep=" , ", end=" ")
        print()

#6-10
def cities():
    
    allCities = {
            
            'Karachi': {
                        'Population':'225400',
                        'Area': '22SQ'
                    },
            'Lahore': {
                        'Population':'115300',
                        'Area':'11SQ'
                    },
            
            'Peshawar': {
                        'Population':'11111',
                        'Area':"9SQ"
                    }
            }
    
    for city, allInfo in allCities.items():
        print(city, end=": \n")
        
        for fact in allInfo:
            print("\t", fact, ":", allInfo[fact], end="\n")
            
            
            
    
    
cities()
    
    
    
    
    
    
    