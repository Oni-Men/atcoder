S = input()

ans = 0

n = len(S)

for i in range(n):
    s = S[i]
    j = ord(s) - ord('A') + 1
    k = n - i - 1
    ans += j * (26 ** k)

print(ans)