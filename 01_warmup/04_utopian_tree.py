"""
Problem Statement: 		Utopian tree doubles in height in spring and increases by 1m in winter. Find height in N growth cycles
Difficulty Level : 		Easy
Time complexity : 		O(1)
Author: 				Shantanu Alshi
"""

testcases = int(input())
while(testcases is not 0):
    ht = 1
    N = int(input())
    
    for i in range(0,N):
    	ht = (ht*2) if (i%2 == 0) else (ht+1)
    
    print(ht)
    testcases = testcases -1
