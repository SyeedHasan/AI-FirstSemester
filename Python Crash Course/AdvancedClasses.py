# C L A S S E S

#9-10 also uses 9-6
from Restaurant import Restaurant
from Restaurant import IceCreamStand

icecreamStand = IceCreamStand("Jamailo", "Ice-cream", ['Chocolate', 'Pineapple'])
icecreamStand.displayFlavors()


#9-11 also uses 9-7 and 9-8
from UserAdminPrivilege import User
from UserAdminPrivilege import Admin
from UserAdminPrivilege import Priviliges

userAdmin = Admin(["Sleep", "Eat", "Dance", "Ban"])
userAdmin.priviliges.showPriviliges()

#9-12 nahi kiya

#9-13
# Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your
# series of print
# statements with a loop that runs through the 
#dictionary’s keys and values.
# When you’re sure that your loop works, add
# five more Python terms to your
# glossary. When you run your program again, 
#these new words and meanings
# should automatically be included in the output.
from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

# for word, definition in glossary.items():
#     print("\n" + word.title() + ": " + definition)



#9-14

from random import randint

class Die():
    """Trying to model real-world dice with 6 sides."""

    def __init__(self, sides=6):
        """Initialize attributes of the class Die."""
        self.sides = sides

    def roll_die(self):
        """Modeling rolling of the die."""
        num = randint(1, self.sides)
        print("The current number on the die is: " + str(num))


# print("\nRolling the 6 sides Die... ")
# six_side_die = Die()
# for i in range(10):
#     six_side_die.roll_die()

# print("\nRolling the 10 sides Die... ")
# ten_side_die = Die(10)
# for i in range(10):
#     ten_side_die.roll_die()

# print("\nRolling the 20 sides Die... ")
# twenty_side_die = Die(20)
# for i in range(10):
#     twenty_side_die.roll_die()


#9-9
#BELOW THE MAIN CODE


# M A I N M E T H O D

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
    	if self.battery_size is not 85:
    		self.battery_size = 85  	  
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


# eCar = ElectricCar("Honda", "Civic", "2017")
# eCar.battery.get_range()
# eCar.battery.upgrade_battery()
# eCar.battery.get_range()