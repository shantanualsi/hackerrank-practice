"""
Problem Statement: 		Convert a string to palindrome if possible return count of changes necessary
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""

def form_palindrome(stringinput):
	count = 0;
	letters = list(stringinput);
	n = len(letters);
	for i in range(0,n/2):
		count = count+abs(ord(letters[i]) - ord(letters[n-i-1]));
	return count;


testcases = int(input());
while testcases is not 0:
	stringinput = str(raw_input());
	print(form_palindrome(stringinput));
	testcases = testcases-1		


"""
Testers code :

t = input()
assert t<=10 and t>=1
for _ in range(t):
    s = list(raw_input())
    assert len(s) >=1 and len(s)<= 10000
    su = 0
    for i in range(0,len(s)/2):
        su+= abs(ord(s[i]) - ord(s[-1-i]))
    print su
"""