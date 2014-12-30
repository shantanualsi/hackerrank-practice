"""
Problem Statement: 		Find average of the candies in jars filled according to the input
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""

# Needs further optimization for large inputs
N,M = raw_input().split(' ');
totalcandies = 0
for i in range(0,int(M)):
	x, y, candies = raw_input().split(' ');
	totalcandies = totalcandies + int(candies) * (int(y)-int(x)+1)

print totalcandies/int(N)

"""
Testers code: 
#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=[int(x) for x in raw_input().split()]
sum1 = 0
for _ in range(m):
    a,b,k=[int(x) for x in raw_input().split() ]
    sum1+=(b-a+1)*k
print  (sum1/n)
"""