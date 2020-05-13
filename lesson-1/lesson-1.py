magic_number = 6
def magic_number_program():
	user_value = input("Enter a number between 0 and 10: ")
	if int(user_value) == magic_number:
		print("Congratulations, you've won.")
	else:
		print("wrong number, please run the program again.")
