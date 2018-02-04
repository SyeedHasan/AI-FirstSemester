
current_users = ['Salman', 'Ehsan', 'Jatoi', 'Junaid', 'Hasan']

new_users = ['Hasan', 'Ahsan', 'Ehsan', 'Muneeb']

#BOOK WALA

# for user in current_users:
# 	user=user.lower()
#Wrong, use the range function from 0 to n
#Assign the variable the lower version
# for user in new_users:
# 	if user in current_users:
# 			print(user + ": Already used!")
# 	else:
# 		print(user + ": Username not used")

#MY IMPLEMENTATION

# for user in new_users:
# 	newUser = user.lower()
# 	for oldUsers in current_users:
# 		if newUser == oldUsers.lower():
# 			print(user + ": Used!")
# 			new_users.remove(user)

# print("Unused names are: " + str(new_users))

#SIR WALA

#AGAIN
# for i in range(0, len(current_users)):
# 	current_users[i] = current_users[i].upper()

# for user in new_users:
# 	if user.upper() in current_users:
# 			print(user + ": Already used!")
# 	else:
# 		print(user + ": Username not used")
