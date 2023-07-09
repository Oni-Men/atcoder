p, q = input().split()
if q < p:
    p, q = q, p

p, q = ord(p) - ord('A'), ord(q) - ord('A')

L = [3, 1, 4, 1, 5, 9]
ans = 0

for i in range(p, min(q, len(L))):
    ans += L[i]

print(ans)
