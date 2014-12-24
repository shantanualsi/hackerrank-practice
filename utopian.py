testcases = int(input())
while(testcases is not 0):
    ht = 1
    N = int(input())
    
    for i in range(0,N):
    	ht = (ht*2) if (i%2 == 0) else (ht+1)
    
    print(ht)
    testcases = testcases -1
