N, K = map(int, input().split())
D = []

total = 0
for i in range(N):
    a, b = map(int, input().split())
    D.append([a, b])
    total += b

D.sort(key=lambda x: x[0])

if total <= K:
    print(1)
    exit()

for a, b in D:
    total -= b
    if total <= K:
        print(a + 1)
        exit()
