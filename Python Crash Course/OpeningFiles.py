
#CHAPTER 10

#Different methods of reading from a file
def Q1():
	with open('python.txt') as fileObject:
		#Entire file read 
		# var = fileObject.read()
		# print(var)

		#Looping over the fileobject
		for line in fileObject:
			print(line.strip())

		#Looping over the content stored in a list
		myList = fileObject.readlines()

	#Using the content outside the 'with block'
	for line in myList:
		print(line.strip())

#Read the content of a file and replace a certain word with 
#something
def Q2():
	filePath = 'python.txt'
	with open(filePath) as fileObject:
		
		for line in fileObject:
			line = line.replace("Dogs", "my DOGS!")
			print(line.strip())


#Write content to a file
def Q3():

	with open('myGuests.txt', 'a') as myFile:
		userName = input("What is your name? - ")
		myFile.write(userName + '\n')


#Write multiple lines in a file recording guest users
def Q4():
	with open('myGuestBook.txt', 'a') as myFile:
		while True:
			userName = input("What is your name? - ")
			if userName == 'Quit':
				break
			print("Hi " + userName + ". Welcome to the Resort!");
			myFile.write(userName + " has checked into the Resort. \n")

def Q5():
	#Incomplete!

#EXCEPTIONS



#Q1()
#Q2()
#Q3()
Q4()


