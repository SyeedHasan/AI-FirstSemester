#Classes
#9-1

class Restaurant():

	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		print("We at " + self.name + " serve " + self.cuisine)

	def open_restaurant(self):
		print("We are open 24/7")

#9-3

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


#Main Code
#9-1
# myR = Restaurant("Hazeem Nihari", "Biryani")
# myR.describe_restaurant();
# myR.open_restaurant();

#9-3
# myUser = User("Syed", "Hasan", 24, "Hameez")
# myUser.describeUser()