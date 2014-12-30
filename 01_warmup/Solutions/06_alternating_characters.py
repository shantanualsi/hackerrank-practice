"""
Problem Statement: 		Find required deletions to make sure there are no consecutive characters same
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""


def replacements(stringinput):
	count = 0;
	prev_char = "";
	for character in stringinput:
		if character == prev_char: 
			count = count+1;
		prev_char = character;
	return count;

testcases = int(input());
while testcases is not 0:
	stringinput = str(raw_input());
	print(replacements(stringinput));
	testcases = testcases-1


"""
Testers code:

t = input()
assert 1 <= t <=10
for _ in range(t):
    s = raw_input()
    assert 1 <= len(s)<= 10**5
    count = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1
    print count
"""