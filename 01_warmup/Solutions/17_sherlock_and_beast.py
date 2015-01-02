
def decent(n):
	count=0;
	if n%3 == 0:
		return count
	while n > 0:
		count = count +1
		n = n-5;
		if(n>=0 and n%3==0):
			return count;
	return -1;


for _ in range(input()):
	N = int(input());
	X = decent(N);
	print 'X = ', X*5, 'Y = ', (N-X*5)
	if(X!=-1):
		print '5' * (N-X*5) + '3' * 5*X
	else:
		print X;
