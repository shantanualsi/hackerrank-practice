testcases = int(input());

while testcases is not 0:
	N, C, W = raw_input().split(' ');
	chocolates = int(N)/int(C);
	wrappers = chocolates;
	while wrappers >= int(W):
		wrappers = wrappers - int(W)+1;
		chocolates = chocolates + 1;
	print chocolates;
	testcases = testcases-1

