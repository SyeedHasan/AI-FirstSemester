
#Problems to understand Exceptions and try-except blocks

import json

def Q6():
	#Calculator with exception of 'TypeError/ValueError'
	#and methods to avoid them
	while True:
		try:
			input1 = input("Enter a number: ")
			
			if input1 == 'q':
				break

			input2 = input("Enter another number: ")

			inputs = int(input1) + int(input2)
		except ValueError:
			print("How ignorant. Enter a number please. No strings!")
			#pass

		else:
			print("Sum = " + str(inputs))

def Q8():
	file1 = 'Cats.txt'
	#Wrong file path to try the except block
	file2 = 'Silento/Dogs.txt'

	files = [file1, file2]

	for file in files:
		#try-except-else block
		try:
			with open(file) as fileObject:
				content = fileObject.read()

		except FileNotFoundError:
			print(file + " was not found!")

		else:
			print("Contents of " + file + " :")
			print(content)

def Q11Part1():
	#Storage using JSON module
	favNum = int(input("Enter your favorite number: "))

	with open("FavoriteNumbers.json", "w") as mainFile:
		json.dump(favNum, mainFile)

def Q11Part2():

	try: 
		with open("FavoriteNumbers.json") as mainFile:
			num = json.load(mainFile)
	except FileNotFoundError:
		print("No such file found!")
	else:
		print("Your favorite number is : " + str(num))



#Test Code (can also be moved to a main function with 
#			proper boilerplate code)

# Q6()
# Q7() - Similar to 6
# Q8()
# Q9() - Similar to 8, use 'pass' in except block
# Q10() - X
# Q11Part1()
# Q11Part2() 
# Q12() - Similar to Q11
