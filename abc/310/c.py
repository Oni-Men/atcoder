N = int(input())
S = [input() for _ in range(N)]

T = set()

for s in S:
    rev = s[::-1]
    if s not in T and rev not in T:
        T.add(s)

print(len(T))
