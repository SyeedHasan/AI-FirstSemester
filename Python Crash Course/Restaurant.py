
# 9 - 6 ka code and aik aur.
# 9-10. Created a separate module for the 
#class and now calling it in
#'AdvancedClasses.py'
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

