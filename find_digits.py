test_cases = int(input())
count=[0]*test_cases;
def is_divisor(user_input, dividend):
	return True if ((float(user_input)/float(dividend)) == float(user_input/dividend)) else False

while(test_cases is not 0):
	input1 = int(input())
	user_input = input1
	dividend = input1
	while input1 != 0:
		dividend = input1%10
		input1 /= 10
		if(dividend is not 0 and is_divisor(user_input,dividend)):
			count[test_cases-1] = count[test_cases-1]+1
	test_cases = test_cases-1

count.reverse();
for i in count: print i;