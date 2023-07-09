N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

P -= 1
R -= 1

print(*(A[:P] + A[R:S] + A[Q:R] + A[P:Q] + A[S:]))
