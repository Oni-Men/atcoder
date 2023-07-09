MAX = 3 * 10 ** 5

ms = []
msprime = [False] * len(ms)
msprime[0] = True

# 月曜土曜数の集める
for i in range(MAX):
    if i % 7 == 1 or i % 7 == 6:
        ms.append(i)

for i in ms:



def solve():
    n = int(input())
    if n == 1:
        return False

    return True


while solve():
    pass
