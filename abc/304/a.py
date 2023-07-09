n = int(input())
s = [""] * n
a = [0] * n

for i in range(n):
    g, h = input().split()
    s[i], a[i] = g, int(h)

young_age = 10**18
young_id = -1

for i in range(n):
    if a[i] < young_age:
        young_age = a[i]
        young_id = i

for i in range(n):
    print(s[(i + young_id) % n])
