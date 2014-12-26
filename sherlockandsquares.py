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
