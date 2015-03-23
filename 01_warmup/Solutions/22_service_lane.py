N, T = raw_input().split()
widths = raw_input().split()
for _ in range(int(T)):
	x=5
	i,j = raw_input().split()
	for lane in range(int(i),int(j)+1):
		if(int(widths[lane]) < x):
			x=int(widths[lane])
	print x