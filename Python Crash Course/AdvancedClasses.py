# C L A S S E S

#9-10 also uses 9-6
from Restaurant import Restaurant
from Restaurant import IceCreamStand

# icecreamStand = IceCreamStand("Jamailo", "Ice-cream", ['Chocolate', 'Pineapple'])
# icecreamStand.displayFlavors()


#9-11 also uses 9-7 and 9-8
from UserAdminPrivilege import User
from UserAdminPrivilege import Admin
from UserAdminPrivilege import Priviliges

userAdmin = Admin(["Sleep", "Eat", "Dance", "Ban"])
userAdmin.priviliges.showPriviliges()

#9-12 nahi kiya

#9-9
#BELOW THE MAIN CODE


# M A I N M E T H O D


"""A set of classes that can be used to represent electric cars."""

"""A class that can be used to represent a car."""

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