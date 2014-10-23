def find_writer(input_line):
	
	text,key = input_line.split("|")
	key_numbers = [int(index) for index in key.strip().split(" ")]
	output = [text[i-1] for i in key_numbers]
	print ''.join(output)

find_writer("osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53")
find_writer("3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA| 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31")