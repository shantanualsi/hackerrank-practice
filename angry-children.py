def min_diff(candies, n,k):
	answer = candies[n-1]
	for i in range(0,n-k):
		minval = candies[i+k-1]-candies[i];
		print ('minval ', minval)
		answer = minval if minval<answer else answer
	return answer


n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()

print min_diff(candies,n,k)
