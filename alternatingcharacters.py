def replacements(stringinput):
	count = 0;
	prev_char = "";
	for character in stringinput:
		if character == prev_char: 
			count = count+1;
		prev_char = character;
	return count;

testcases = int(input());
while testcases is not 0:
	stringinput = str(raw_input());
	print(replacements(stringinput));
	testcases = testcases-1
