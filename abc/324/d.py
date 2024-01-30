N = int(input())
S = input()

ans = 0

S = sorted(S)

for i in range(int(10 ** 6.6)):
    s = str(i ** 2).zfill(N)
    s = sorted(s)
    if s == S:
        ans += 1

print(ans)
