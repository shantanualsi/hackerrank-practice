"""
Problem Statement: 		Maximum pieces for given number of cuts
Difficulty Level : 		Easy
Time complexity : 		O(1)
Author: 				Shantanu Alshi
"""


testcases = int(input());

while testcases is not 0:
	slices = int(input());
	# Representing input as addition of numbers -
	evenslices = slices/2;
	if(slices%2 == 0):
		print(evenslices**2);
	else:
		print evenslices*(evenslices+1)
	testcases = testcases-1

"""
Testers code:

T = input()
assert 1 <= T <= 10
for i in range(T):
    K = input()
    assert 1 <= K <= 10**7
    if K % 2 == 0:
        print (K/2)*(K/2)
    else:
        print (K/2)*(K/2+1)
"""
