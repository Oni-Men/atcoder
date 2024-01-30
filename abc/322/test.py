import bisect


A = [1, 3, 3, 3, 5]

i = bisect.bisect_left(A, 4) - 1
print(i)