from collections import deque

K = int(input())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


ans = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        g1 = gcd(a, b)
        if g1 == 1:
            ans += K
        else:
            for c in range(1, K+1):
                g2 = gcd(g1, c)
                ans += g2

print(ans)
