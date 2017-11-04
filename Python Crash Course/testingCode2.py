import unittest

#Exercises 11-3
#Using pythons 'unittest' for testing code

class Employee():

	def __init__(self, firstName, lastName, salary):
		self.firstName = firstName
		self.lastName = lastName
		self.salary = salary

	def give_raise(self, amount='5000'):
		self.salary += int(amount)
		return self.salary

class testEmployee(unittest.TestCase):

	def setUp(self):
		self.employee = Employee("Syed", "Hasan", 25000)

	def test_give_default_raise(self):
		currentSalary = self.employee.give_raise()
		print("Your salary: " + str(currentSalary))
		self.assertEqual(currentSalary, 30000)

	def test_give_custom_raise(self):
		currentSalary = self.employee.give_raise(25000)
		print("Your salary: " + str(currentSalary))
		self.assertEqual(currentSalary, 50000)

unittest.main()