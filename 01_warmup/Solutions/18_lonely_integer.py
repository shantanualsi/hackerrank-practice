pairs = dict()
number_of_elements = input()

array = raw_input().split(' ')

for num in array:
	if num in pairs:
		pairs[num] = pairs[num]+1
	else:
		pairs[num] = 1

for i in pairs:
	if pairs[i] == 1:
		print i