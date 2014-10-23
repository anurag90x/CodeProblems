def set_intersection(number_sets):
	'''
	Find the intersection of 2 sorted lists
	
	'''

	first_set,second_set = number_sets.strip().split(";")
	first_set = [int(num) for num in first_set.split(",")]
	second_set = [int(num) for num in second_set.split(",")]
	intersection = []
	done = False
	start_l1 = 0
	start_l2 = 0
	while not done:
		if first_set[start_l1] == second_set[start_l2]:
			intersection.append(str(first_set[start_l1]))
			start_l1 += 1
			start_l2 += 1
		elif first_set[start_l1] < second_set[start_l2]:
			start_l1 += 1
		else:
			start_l2 += 1
		# finished traversing one of the lists
		if start_l1 > len(first_set)-1 or start_l2 > len(second_set)-1:
			done = True
	if not intersection:
		print '\n'
	else:
		print ','.join(intersection)

set_intersection("7,8,9;8,9,10,11,12")