n = int(input())

a = int(n / 5) * 5
b = (int(n / 5) + 1) * 5

if abs(n - a) < abs(n - b):
    print(a)
else:
    print(b)
