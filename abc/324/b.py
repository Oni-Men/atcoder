N = int(input())

ans = True

i = N
while i % 2 == 0:
    i = i // 2

while i % 3 == 0:
    i = i // 3

if i != 1:
    ans = False

print("Yes" if ans else "No")
