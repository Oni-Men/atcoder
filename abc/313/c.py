N = int(input())
A = list(map(int, input().split()))

min_val = min(A)
max_val = max(A)

ans = 0

while max_val - min_val > 1:
    

print(ans)