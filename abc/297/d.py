A, B = map(int, input().split())

ans = 0

while A != B:
    if A > B:
        if A % B == 0:
            ans += A // B - 1
            break
        else:
            i = A // B
            A -= B * i
            ans += i
    else:
        if B % A == 0:
            ans += B // A - 1
            break
        else:
            i = B // A
            B -= A * i
            ans += i

print(ans)
