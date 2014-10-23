def trailing_string(input_line):
	'''
	Check if the second string is the last part of the first string (trailing)

	'''
	first_string,second_string = input_line.strip().split(",")
	if len(second_string) > len(first_string):
		return 0
	start_index = len(first_string)-len(second_string)
	return 1 if first_string[start_index:] == second_string else 0

print trailing_string("Hello World,World")
print trailing_string("Hello CodeEval,CodeEval")
print trailing_string("San Francisco,San Jose")



