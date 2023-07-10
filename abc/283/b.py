N = int(input())
A = list(map(int, input().split()))
Q = int(input())

queries = [input() for _ in range(Q)]

for i in range(Q):
	qlist = queries[i].split()
	op = qlist[0]
	k = int(qlist[1]) - 1
	if op == '1':
		A[k] = int(qlist[2])
	if op == '2':
		print(A[k])