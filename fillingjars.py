# Needs further optimization for large inputs
N,M = raw_input().split(' ');
totalcandies = 0
for i in range(0,int(M)):
	x, y, candies = raw_input().split(' ');
	totalcandies = totalcandies + int(candies) * (int(y)-int(x)+1)

print totalcandies/int(N)
