def insertionSort(ar):    
	# Determine the unsorted one
	for x in xrange(1, len(ar)):
		curr_val = ar[x]
		pos = x
		while pos > 0 and ar[pos-1]>curr_val:
			ar[pos] = ar[pos-1]
			pos -=1
		ar[pos] = curr_val
		print ' '.join(map(str,ar))
	return ar

inputSize = int(raw_input());
# ar = [int(i) for i in raw_input().strip().split()]
ar = map(int,raw_input().split());
# print ' '.join(map(str,insertionSort(ar)))
insertionSort(ar)