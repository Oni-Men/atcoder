import sys
sys.setrecursionlimit(10 ** 4)

def permutation(list_p, list_r=[], ans=[]):
    if not list_p:
        ans.append(list_r)
    else:
        for i in range(len(list_p)):
            next_r = [*list_r]
            next_p = [*list_p]
            next_r.append(list_p[i])
            del next_p[i]
            permutation(next_p, next_r, ans)
    return ans

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


P = [i for i in range(6)]
for p in permutation(P):
    print(p)