from math import log

def predict_next(num):
	'''
	Predict the value of a particular index. 
	Recursively calls itself using the difference in values between the number and the nearest exponent of 2.

	'''

	if num == 0:
		return 0
	num_log = int(log(num,2))
	return get_complement(predict_next(num-2**num_log))

def get_complement(number):
	'''
	Function to return the appropriate value based on the value passed in.

	'''
	return 1 if number == 0 else 2 if number == 1 else 0

# few simple tests

print predict_next(0)
print predict_next(5)
print predict_next(101)
print predict_next(25684)
