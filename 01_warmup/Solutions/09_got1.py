"""
Problem Statement: 		Determine if an anagram has a palindrome
Difficulty Level : 		Easy
Time complexity : 		O(n)
Author: 				Shantanu Alshi
"""

string = raw_input()
 
def has_palindrome(string):
	flag = True;
	odd_count = 0;
	if(len(string)%2 == 1):
		# If string length is odd, exactly one character should be odd in number.
		for i in set(string):
			count = string.count(i);
			if(count%2 == 1):
				odd_count = odd_count + 1;
				if(odd_count > 1):
					flag = False;
	else:
		# If string length is even, no character count should be odd.
		for i in set(string):
			count = string.count(i);
			if(count%2 == 1):
				flag = False;
	return flag;
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

if not has_palindrome(string):
    print("NO")
else:
    print("YES")


"""
Testers code:

n,m = [int(x) for x in raw_input().split()]
maxi = 0
cnt = 0
inp = [raw_input() for _ in range(n)]
for i in range(0,n):
    for j in range(i+1,n):
        set_bit = bin(int(inp[i],2) | (int(inp[j],2))).count("1")
        if set_bit>maxi:
            maxi = set_bit
            cnt = 1
        elif set_bit == maxi:
            cnt+=1
print maxi
print cnt
"""