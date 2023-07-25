N = int(input())

dp = {}


def get(n):
    if n == 0:
        return 1
    if n in dp:
        return dp[n]
    dp[n] = get(n // 2) + get(n // 3)
    return dp[n]


print(get(N))
