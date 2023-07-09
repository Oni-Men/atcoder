n = int(input())

for i in range(3, 9):
    if n <= 10 ** 3 - 1:
        print(n)
        break
    elif 10 ** i <= n <= 10 ** (i + 1) - 1:
        print(n - (n % 10 ** (i-2)))
        break
