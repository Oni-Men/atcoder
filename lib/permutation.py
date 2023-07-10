def prev_permutation(p: list | tuple):
    n = len(p)
    i = n-2
    while p[i] < p[i+1]:
        i -= 1

    j = n - 1
    while p[i] < p[j]:
        j -= 1

    p[i], p[j] = p[j], p[i]
    return p[:i+1] + p[:i:-1]


P = [4, 3, 2, 1]
for i in range(24):
    print(P)
    P = prev_permutation(P)
