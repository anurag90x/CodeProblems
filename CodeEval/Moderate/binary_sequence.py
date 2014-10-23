def binary_seq(input_string):
	bin_seq, char_seq = input_string.strip().split(" ")
	check_equivalence(bin_seq,char_seq,0,0)

def check_equivalence(bin_seq,char_seq,bin_index,char_index):

	while keep_going(args):
		if not check_equivalence(bin_seq,char_seq,bin_index+1,char_index+1):
			check_equivalence(bin_seq,char_seq,bin_index,char_index+1)



def mapping(bin,char):

	return_value = True if bin=='0' and set(char)=='A' or bin=='1' and set(char)=='B' or set(char)=='A' else False
	return return_value