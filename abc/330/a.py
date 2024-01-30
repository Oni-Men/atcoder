N, L = map(int, input().split())
A = list(map(int, input().split()))

ans = len(list(filter(lambda x: x >= L, A)))
print(ans)