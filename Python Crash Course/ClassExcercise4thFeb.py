
#Class named 'Computer' with name, brand, processor speed.
#Two class association with 'Hardware' and 'Software'
class Computer():

	def __init__(self, name, brand, procSpeed):
		self.name = name
		self.brand = brand
		self.procSpeed = procSpeed
		# self.hardware = Hardware('MSI', '2.3GHz')
		# self.software = Software('23-11-2017', 'Online', 'MS Office', 'XAMPP', 'FlyWheel', 'Excel', 'Ubuntu')
		self.hardware = [Hardware('MSI', '2.3GHz')]
		self.software = [Software('23-11-2017', 'Online', 'MS Office', 'XAMPP', 'FlyWheel', 'Excel', 'Ubuntu')]

	def addHardware(self, name, specs):
		self.hardware.append(Hardware(name, specs))

	def addSoftware(self, date, status, *softNames):
		soft = list(softNames)
		self.software.append(Software(date, status, soft))

	def displayComputerInfo(self):
		print("Name: " + str(self.name))
		print("Brand: "+ str(self.brand))
		print("Processor Speed: " + str(self.procSpeed))

class Hardware():

	def __init__(self, name, specs):
		self.name = name
		self.specs = specs

	def displayHardware(self):
		print()
		print("Available hardware information: ", end="\n")
		print("Name: " + str(self.name) + "- Specfications: " + str(self.specs))

class Software():

	def __init__(self, date, info, *softNames):
		self.softwareNames = list(softNames)
		self.date = date
		self.info = info

	def displaySoftwares(self):
		print()
		print("Date Installed: " + str(self.date))
		print("Information Available: " + str(self.info))
		print("Software available: " + str(self.softwareNames))


comp = Computer('Hasans PC', 'HP', '2.3GHz')
comp.displayComputerInfo()
print("")
comp.addSoftware('23-12-2018', 'offline', 'PowerPoint')
for i in comp.hardware:
	i.displayHardware()

for i in comp.software:
	i.displaySoftwares()