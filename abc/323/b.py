N = int(input())

ranking = [[0, i+1] for i in range(N)]

for i in range(N):
    S = input()
    for j in range(N):
        if i == j:
            continue
        if S[j] == 'x':
            ranking[i][0] += 1
        else:
            ranking[j][0] += 1

ranking = sorted(ranking, key=lambda t: t[0])
print(*map(lambda t: t[1], ranking))
