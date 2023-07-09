from math import sqrt, ceil

R, X, Y = map(int, input().split())

R = R ** 2
D = X ** 2 + Y ** 2

if D == R:
    ans = 1
elif D <= 4 * R:
    ans = 2
else:
    ans = ceil(sqrt(D / R))

print(ans)
