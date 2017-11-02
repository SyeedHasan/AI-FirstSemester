
# C L A S S E S

#9-6
class Restaurant():

	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		print("We at " + self.name + " serve " + self.cuisine)

	def open_restaurant(self):
		print("We are open 24/7")

class IceCreamStand(Restaurant):

	def __init__(self, name, cuisine, flavors):
		super().__init__(name,cuisine)
		self.flavors = flavors

	def displayFlavors(self):
		print("Flavors: " + str(self.flavors))


#9-7

class User():

	def __init__(self, firstName, lastName, age, whereFrom):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.whereFrom = whereFrom

	def describeUser(self):
		print("User Details:")
		print("Name:".rjust(10) + self.firstName + " " + self.lastName)
		print("Age:".rjust(9) + str(self.age))
		print("City:".rjust(10) + self.whereFrom)

class Admin(User):

	def __init__(self, priviliges):
		# Add super--- if needed.
		self.priviliges = Priviliges(priviliges)


class Priviliges():
	
	def __init__(self, priviliges):
		self.priviliges = priviliges

	def showPriviliges(self):
			print("Priviliges: " + str(self.priviliges))

# M A I N M E T H O D

# icecreamStand = IceCreamStand("Jamailo", "Ice-cream", ['Chocolate', 'Pineapple'])
# icecreamStand.displayFlavors()

# userAdmin = Admin(["Ban", "Eat", "Sleep"])
# userAdmin.showPriviliges()

userAdmin = Admin(["Sleep", "Eat", "Dance", "Ban"])
userAdmin.priviliges.showPriviliges()