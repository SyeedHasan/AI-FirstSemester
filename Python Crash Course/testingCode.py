#Chapter 11 Exercises

import unittest

def cityCountry(city, country, population=''):
	if population:
		return city + " , " + country + " - Population " + population
	else:
		return city + " , " + country 

class testingCityCountry(unittest.TestCase):

	def test_cityCountry(self):
		got = cityCountry("Karachi", "Pakistan")
		self.assertEqual(got, "Karachi , Pakistan")

	def test_population(self):
		got = cityCountry("Karachi", "Pakistan", "22350000")
		self.assertEqual(got, "Karachi , Pakistan - Population 22350000")


unittest.main()

