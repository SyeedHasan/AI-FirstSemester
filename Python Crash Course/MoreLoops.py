
myList = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Fandango']
mySecList = myList[:]
mySecList.append("Xavier")

for terms in myList:
    print(terms)

for terms in mySecList:
    print(terms, end=" ")