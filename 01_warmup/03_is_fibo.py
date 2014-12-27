"""
Problem Statement: 		You are given an integer, N. Write a program to determine if N is an element of the Fibonacci Sequence.
Difficulty Level : 		Easy
Time complexity : 		O(n) - computing the set, O(1) - Set lookup
Author: 				Shantanu Alshi
"""


# The range of fibonacci series in the problem given is 10**10. The 60th fibo itself is 60 digits long. 
# Lets calculate all fibonacci numbers and store them in a set for lookup in O(1) 
# Can also use Binary search but that would be O(nlogn)

fibo = set()
def generate_fibo():
	thisnumber = 1
	prevnumber = 1
	while thisnumber < 10000000000:
		fibo.add(thisnumber)
		currentnumber = thisnumber + prevnumber
		prevnumber, thisnumber = thisnumber, currentnumber

# Generate all fibonacci numbers first
generate_fibo()

testcases = int(input())
while(testcases is not 0):
	num = int(input())
	print("IsFibo") if (num in fibo) else print("IsNotFibo") 
	testcases = testcases - 1


"""
The problem with this Solution is that it uses floating point numbers that may sometimes lead to incorrect results due to precision errors
Solution: O(1)
from math import *
for i in range(input()):
    n=input()
    r1 = sqrt(5*n**2+4)
    r2 = sqrt(5*n**2-4)
    isSquare = r1%1 == 0 or r2%1==0
    if(isSquare):
        print "IsFibo"
    else:
        print "IsNotFibo"
"""