"""
Problem Statement: 		Find how many choclates can one have if W wrappers can be exchanged for 1 candy 
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""

testcases = int(input());

while testcases is not 0:
	N, C, W = raw_input().split(' ');
	chocolates = int(N)/int(C);
	wrappers = chocolates;
	while wrappers >= int(W):
		wrappers = wrappers - int(W)+1;
		chocolates = chocolates + 1;
	print chocolates;
	testcases = testcases-1

