def unique_elements(string):
	'''
	Get only the unique elements from the sorted list

	'''
	sorted_array = string.strip().split(",")
	unique_array = []
	for element in sorted_array:
		if not unique_array or unique_array[-1] != element:
			unique_array.append(element)
	print ','.join(unique_array)

unique_elements("1,1,1,2,2,3,3,4,4")