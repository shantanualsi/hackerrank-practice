def form_palindrome(stringinput):
	count = 0;
	letters = list(stringinput);
	n = len(letters);
	for i in range(0,n/2):
		count = count+abs(ord(letters[i]) - ord(letters[n-i-1]));
	return count;


testcases = int(input());
while testcases is not 0:
	stringinput = str(raw_input());
	print(form_palindrome(stringinput));
	testcases = testcases-1		