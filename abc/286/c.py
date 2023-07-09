n, a, b = map(int, input().split())
s = input()

ans = 10 ** 18

for i in range(n):
    cost = 0
    for j in range(n//2):
        if s[j] != s[n - j - 1]:
            cost += b
    ans = min(ans, cost + a * i)
    s = s[1:] + s[0]

print(ans)
