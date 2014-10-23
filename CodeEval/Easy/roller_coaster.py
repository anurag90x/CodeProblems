def roller_coaster(text):
	'''
	Function to make lower case characters upper case and vice versa

	'''
	lines = text.split("\n")
	for line in lines:
		new_line = ""
		for index,char in enumerate(line):
			if char.isalpha():
				if index==0:
					# first character has to be upper case
					char = char.upper()
				else:
					char = char.upper() if last_character.islower() else char.lower()
				last_character = char

			new_line += char
		print new_line