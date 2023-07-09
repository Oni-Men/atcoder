from itertools import permutations

n, m = map(int, input().split())
S = [input() for _ in range(n)]


def almost_equal(a, b):
    count = 0
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return count == 1


ans = False

for p in permutations(S):
    tmp = True
    for i in range(n-1):
        if not almost_equal(p[i], p[i-1]):
            tmp = False
    ans |= tmp

print("Yes" if ans else "No")
