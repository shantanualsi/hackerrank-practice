"""
Problem Statement: 		You are given an integer N. Find the digits in this number that exactly divide N and display their count. For N = 24, 
						there are 2 digits - 2 & 4. Both these digits exactly divide 24. So our answer is 2.
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""

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


"""
SOLUTION: 

Complexity : O(n)
for _ in range(input()):
    a=input()
    count = 0
    for i in list(str(a)):
        if int(i)!=0 and a%int(i)==0:
            count+=1
    print count

"""