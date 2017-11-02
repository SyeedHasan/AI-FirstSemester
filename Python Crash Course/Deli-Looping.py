
#7-8

def deli():
    sandwichOrders = ['Hoggie', 'Hoagie', 'Hoga']
    finishedSandwiches = []
    
    while sandwichOrders:
        order = sandwichOrders.pop();
        print("I made your " + order + " sandwich");
        finishedSandwiches.append(order);
    
    print("Finished Sandwiches are: ")
    for sandwich in finishedSandwiches:
        print(sandwich);

#7-9

def pastrami():
    print("No pastrami!")
    sandwichOrders = ['Hoggie', 'Pastrami', 'Pastrami', 'Hoagie', 'Hoga', 'Pastrami']
    while 'Pastrami' in sandwichOrders:
        sandwichOrders.remove('Pastrami')
        
    finishedSandwiches = sandwichOrders
    print(finishedSandwiches)
   
#7-10

def dreamVac():
    while True:
        message = "What is the location you would love to visit? "
        userAns = input(message)
        
        print(userAns + " is a beautiful place to visit indeed!")
        userAns = input("Would you like to try again? ")
        
        if userAns == 'No':
            break
    
    
dreamVac()  