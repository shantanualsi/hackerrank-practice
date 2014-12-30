"""
Problem Statement: 		Number on nth stone if difference between consecutive stones is either a or b
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""


for _ in range(input()):
	values = set();
	n = int(input());
	a = int(input());
	b = int(input());

	for i in range(0,n):
		last_stone = i*a+(n-1-i)*b;
		values.add(last_stone);
	print ' '.join(map(str, list(sorted(values))));


"""
Problem Testers code:

for _ in range(input()):
s=set()
n=input();a=input();b=input()
for i in range(0,n):
	s.add(i*a+ (n-i-1)*b)
s= list(s)
s=sorted(s)
s= map(str,s)
print ' '.join(s)
"""