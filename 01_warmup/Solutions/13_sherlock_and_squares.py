"""
Problem Statement: 		How many perfect squares between a range of numbers
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""

import math;
testcases = int(input());

while testcases is not 0:
	A,B = raw_input().split(' ');
	nearest_square_A = math.ceil(math.sqrt(int(A)))**2;
	nearest_square_B = math.floor(math.sqrt(int(B)))**2;
	count = 0;
	i=nearest_square_A;
	
	while i <=int(nearest_square_B):
		count = count+1;
		i = (i) + (2*math.sqrt(i) + 1);
		
	print count;
	testcases = testcases-1


"""
Testers code: 
from math import *
t = input()
assert t<=100
for _ in range(t):
    a,b=[int(x) for x in raw_input().split()]
    assert a<=10**9 and b<=10**9 and a>=1 and b>=1
    a=ceil(sqrt(a));b=floor(sqrt(b))
    print int(b-a)+1

O(1) method - take sqrt(a) and sqrt(b), count the number of integers between them
"""