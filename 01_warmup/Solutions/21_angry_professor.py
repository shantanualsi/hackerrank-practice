for _ in range(int(raw_input())):
	present = 0
	num, min_students = raw_input().split(' ')
	arrivals = raw_input().split()

	for tme in arrivals:
		if int(tme)<=0:
			present = present + 1

	if present < int(min_students):
		print 'YES'
	else:
		print 'NO'

