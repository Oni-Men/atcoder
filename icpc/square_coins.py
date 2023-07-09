dp = [1] * 300
for i in range(2, 18):
    for j in range(i ** 2, 300):
        dp[j] += dp[j-i**2]


def solve():
    n = int(input())
    if n == 0:
        return False
    print(dp[n])
    return True


while solve():
    pass
