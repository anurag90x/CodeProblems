import string

def find_pangram(text):
	'''
	 Checks if a sentence has all the characters in the alphabet else print the sorted list of missing characters

	'''

	all_letters = string.lowercase
	char_dict = {}
	for char in text:
		if char.isalpha():
			if char.lower() not in char_dict:
				char_dict[char.lower()] = ''
	if len(set(list(all_letters))-set(char_dict.keys())) ==0:
		print "NULL"
	else:
		missing = list(set(list(all_letters)) - set(char_dict.keys()))
		missing = sorted(missing,key=lambda val: ord(val))
		print ''.join(list(missing))

find_pangram("A quick brwn fx jumps ver the lazy d")
