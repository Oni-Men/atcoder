MAX = 10**6 + 1000

dp = [i for i in range(MAX)]
dp_odd = [i for i in range(MAX)]

def minv(a, b):
    return a if a < b else b

# x: xまでの正四面体数がつかえる
for x in range(2, MAX):
    k = x * (x + 1) * (x + 2) // 6
    if k >= 10 ** 6:
        break
    for i in range(k, MAX):
        if i - k >= 0:
            dp[i] = minv(dp[i], dp[i-k]+1)
            if k & 1 == 1:
                dp_odd[i] = minv(dp_odd[i], dp_odd[i-k]+1)

ans = []

def solve():
    n = int(input())
    if n == 0:
        return False
    ans.append((dp[n], dp_odd[n]))
    return True


while solve():
    pass

for t in ans:
    print(t[0], t[1]) 
