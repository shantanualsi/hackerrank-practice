"""
Problem Statement: 		Find the pair that gives the maximum xor in a given range of numbers
Difficulty Level : 		Easy
Time complexity : 		O(n2)
Author: 				Shantanu Alshi
"""


#!/usr/bin/python3
def maxXor(L, R):
	maxval = 0
	for i in range (L,R):
		for j in range (L,R):
			xorresult = i^j
			if(xorresult > maxval):
				maxval = xorresult
	return maxval

        
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  if(l>r):
  	print("error")
  print(maxXor(l, r))


"""
Solution:
def maxXOR(L,R):
P = L^R
ret = 1
while(P): # this one takes (m+1) = O(logR) steps
    ret <<= 1
    P >>= 1
return (ret - 1)

print(maxXOR(int(input()),int(input())))
"""