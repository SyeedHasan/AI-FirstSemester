
#Separated module for exc 9-11
#Their test cases are in AdvancedClasses.py

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

#9-8

class Priviliges():
	
	def __init__(self, priviliges):
		self.priviliges = priviliges

	def showPriviliges(self):
			print("Priviliges: " + str(self.priviliges))
