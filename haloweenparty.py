testcases = int(input());

while testcases is not 0:
	slices = int(input());
	# Representing input as addition of numbers -
	evenslices = slices/2;
	if(slices%2 == 0):
		print(evenslices**2);
	else:
		print evenslices*(evenslices+1)
	testcases = testcases-1
