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


#9-2
#Three instances of the class
r1 = Restaurant("Hama", "Jalebi");
r2 = Restaurant('Hameem', 'Cuisine');
r3 = Restaurant('Hasan', 'Urik');


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


#9-4
class Restaurant():

	def __init__(self, name, cuisine, number_served=0):
		self.name = name
		self.cuisine = cuisine
		self.number_served = number_served

	def describe_restaurant(self):
		print("We at " + self.name + " serve " + self.cuisine)

	def open_restaurant(self):
		print("We are open 24/7")

	def set_number_served(self):
		print("Number of customers served: " + str(self.number_served));

	def increment_number_served(self, num):
		num += 1
		print("Number served: " + str(num));


#9-5

class User():

	def __init__(self, firstName, lastName, age, whereFrom, login_attempts):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.whereFrom = whereFrom
		self.login_attempts = login_attempts

	def describeUser(self):
		print("User Details:")
		print("Name:".rjust(10) + self.firstName + " " + self.lastName)
		print("Age:".rjust(9) + str(self.age))
		print("City:".rjust(10) + self.whereFrom)

	def increment_login_attempts(self):
		self.login_attempts += 1
		print("Login Attempts: " + str(self.login_attempts));

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("Reset login attempts.")

#Main Code
#9-1
# myR = Restaurant("Hazeem Nihari", "Biryani")
# myR.describe_restaurant();
# myR.open_restaurant();

#9-3
# myUser = User("Syed", "Hasan", 24, "Hameez")
# myUser.describeUser()

#9-4
# R = Restaurant('Nihari Wala', 'Nihari', 24)
# R.set_number_served();
# R.increment_number_served(33);

#9-5
myUser = User("Syed", "Hasan", 24, "Hameez", 2)
myUser.describeUser()
myUser.increment_login_attempts();
myUser.reset_login_attempts();