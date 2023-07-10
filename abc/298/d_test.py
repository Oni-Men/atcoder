N = 4 * 10**5
print(N + 1)
for i in range(N):
  if i % 7 == 0:
    print("2")
  else:
    print(f"1 {i % 10}")
print("3")