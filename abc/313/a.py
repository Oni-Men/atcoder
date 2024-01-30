N = int(input())
P = list(map(int, input().split()))

max_p = max(P)
count_max = len(list(filter(lambda x: x == max_p, P)))

if count_max == 1 and P.index(max_p) == 0:
    print(0)
else:
    print(max_p + 1 - P[0])
