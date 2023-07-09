N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

priceByColor = {}

for i in range(M):
    priceByColor[D[i]] = P[i+1]

ans = 0

for c in C:
    if c in priceByColor:
        ans += priceByColor[c]
    else:
        ans += P[0]


print(ans)
