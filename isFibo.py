fibo = set()

def generate_fibo():
	thisnumber = 1
	prevnumber = 1
	while thisnumber < 10000000000:
		fibo.add(thisnumber)
		currentnumber = thisnumber + prevnumber
		prevnumber, thisnumber = thisnumber, currentnumber

generate_fibo()
testcases = int(input())
while(testcases is not 0):
	num = int(input())
	print("IsFibo") if (num in fibo) else print("IsNotFibo") 
	testcases = testcases - 1
