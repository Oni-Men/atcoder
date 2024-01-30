N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

ans = []


def check_stsr(s1, s2):
    i = 0
    while i < min(len(s1), len(s2)):
        if s1[i] != s2[i]:
            break
        i += 1

    cond1 = s1[:i] == s2[:i]
    cond2 = False
    if len(s1) < len(s2):
        cond2 = s1[i:] == s2[i+1:]
    else:
        cond2 = s1[i+1:] == s2[i:]
    return cond1 and cond2


for i in range(N):
    s = S[i]
    if s == T:
        ans.append(i)
        continue

    if abs(len(T) - len(s)) == 1:
        if check_stsr(s, T):
            ans.append(i)

    if len(s) == len(T):
        ok = True
        diff = 0
        for s1, s2 in zip(s, T):
            if s1 == s2:
                continue
            diff += 1
            if diff > 1:
                ok = False
                break
        if ok:
            ans.append(i)

# 答え出力
print(len(ans))
print(*map(lambda x: x + 1, ans))
