def reverse_sentence():
	'''
	Function that reads a test file and reverses the sentences
	'''

	test_cases = open(sys.argv[1], 'r')
	for test in test_cases.readlines():
		words = test.strip().split(" ")
		new_sent = []
		for word in reversed(words):
			new_sent.append(word)
		print " ".join(new_sent)

	test_cases.close()
