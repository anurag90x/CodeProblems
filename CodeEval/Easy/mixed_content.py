
def mixed_content(content):
	'''
	Separate the words and numbers

	'''

	content_elements = content.split(",")
	word_list = []
	number_list = []
	for element in content_elements:
		word_list.append(element) if element.isalpha() else number_list.append(element)
	print ",".join(word_list)+"|"+",".join(number_list)

mixed_content("8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21,24,13,14,43,41")