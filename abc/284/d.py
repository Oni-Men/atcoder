T = int(input())
Ts = [int(input()) for _ in range(T)]

def find(n):
	p, q = 0, 0
	for i in range(2, n):
		if n % i != 0:
			continue
		if (n / i) % i == 0:
			p = i
			q = n / (p * p)
		else:
			q = i
			p = (n / q) ** (1/2)
		break
	return int(p), int(q)

for n in Ts:
	p, q = find(n)
	print("{0} {1}".format(p, q))