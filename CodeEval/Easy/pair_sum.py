
def find_sum(num_list):
	'''
	Find all pairs that sum to the same value

	'''

	numbers, sum_value = num_list.split(";")
	numbers = [int(num) for num in numbers.strip().split(",")]
	start_ind = 0
	end_ind = len(numbers)-1
	pair_list = []
	sum_value = int(sum_value)
	while start_ind <= end_ind:
		summation = numbers[start_ind]+numbers[end_ind] 
		if summation == sum_value :
			pair = str(numbers[start_ind])+","+str(numbers[end_ind])
			pair_list.append(pair)
			start_ind += 1
			end_ind -= 1
		elif summation > sum_value:
			# if the present sum is greater than the sum required then move back (decrementing sum)
			end_ind -= 1
		else:
			start_ind += 1
	if pair_list:
		pair_list = sorted(list(set(pair_list)),key=lambda val: int(val[0]))
		print ";".join(pair_list)
	else:
		print "NULL"


find_sum("1,1,2,3,4,4,6;5")
find_sum("2,4,5,6,9,11,15;20")
find_sum("1,2,3,4;50")