searchq = int(input());
_ = int(input());
input_array = raw_input().split(' ');

print input_array
for index, i in enumerate(input_array):
	print ' i = ', i, 'index = ' ,index
	if int(i) == searchq:
		print index;
		break;

