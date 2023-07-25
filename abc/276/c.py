N = int(input())
P = list(map(int, input().split()))


def prev_permutation(p):
    n = len(p)
    i = n-2
    while p[i] < p[i+1]:
        i -= 1

    j = n - 1
    while p[i] < p[j]:
        j -= 1

    p[i], p[j] = p[j], p[i]
    return p[:i+1] + p[:i:-1]


print(*prev_permutation(P))
