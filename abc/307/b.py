N = int(input())
S = [""] * N

for i in range(N):
    S[i] = input()


def check(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return check(s[1:-1])


ans = False

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if check(S[i] + S[j]):
            ans = True

print("Yes" if ans else "No")
