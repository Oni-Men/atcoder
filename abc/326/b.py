N = int(input())

def is326(x):
  a = (x % 1000) // 100
  b = (x % 100) // 10
  c = (x % 10) // 1
  return a * b == c

i = N

while not is326(i):
  i += 1

print(i)