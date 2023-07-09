X, K, D = map(int, input().split())
X = abs(X)

if X - K*D > 0:
    print(X - K*D)
else:
    n = X//D
    if (K-n) % 2 == 0:
        print(X % D)
    else:
        print(abs(X % D - D))
