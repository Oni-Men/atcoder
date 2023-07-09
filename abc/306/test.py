f = {
    1: 5,
    2: 4,
    3: 7,
    4: 8
}

l = [1, 2, 3, 4]

print(sorted(l, key=lambda x: f[x]))
