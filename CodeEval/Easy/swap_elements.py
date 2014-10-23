def swap_elements(text):
	'''
	Swap elements in the specified index range
	
	'''
	value_list, split_ranges = text.split(":")
	value_list = value_list.strip().split(" ")
	split_ranges = split_ranges.split(",")
	for split in split_ranges:
		start, end = map(lambda val: int(val),split.strip().split("-"))
		temp = value_list[start]
		value_list[start] = value_list[end]
		value_list[end] = temp
	print ' '.join(value_list)

swap_elements("1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3")