
for _ in range(int(raw_input())):
	input_num = "{0:b}".format(int(raw_input())).zfill(32)
	flipped_num = ''.join('1' if x== '0' else '0' for x in input_num)  
	print int(flipped_num,2)

