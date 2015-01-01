# Function that finds the GCD of two numbers
# Function Binary GCD is taken from Donald Knuth's art of programming book
def gcd_bin(u, v):
    u, v = abs(u), abs(v) # u >= 0, v >= 0
    if u < v:
        u, v = v, u # u >= v >= 0
    if v == 0:
        return u 
    # u >= v > 0
    k = 1
    while u & 1 == 0 and v & 1 == 0: # u, v - even
        u >>= 1; v >>= 1
        k <<= 1
 
    t = -v if u & 1 else u
    while t:
        while t & 1 == 0:
            t >>= 1
        if t > 0:
            u = t
        else:
            v = -t
        t = u - v
    return u * k


def has_coprime(data):
	input_gcd = 0;
	for i in data:
		input_gcd = gcd_bin(int(i),input_gcd);
		if input_gcd==1:
			return 'YES';
	return 'NO';


for _ in range(input()):
	input_gcd = 0;
	size = int(input());
	data = raw_input().split(' ');
	print has_coprime(data);
