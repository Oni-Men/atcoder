N, X, Y = map(int, input().split())

N -= 1

red = [0] * 10
blue = [0] * 10

red[N] = 1

state = 0

while True:
    if all([e == 0 for e in red[1:]]):
        state += 1
    else:
        for i in range(9):
            if red[9 - i] != 0:
                red[8 - i] += red[9 - i]
                blue[9 - i] += X * red[9 - i]
                red[9 - i] = 0
                break
    if all([e == 0 for e in blue[1:]]):
        state += 1
    else:
        for i in range(9):
            if blue[9 - i] != 0:
                red[8 - i] += blue[9 - i]
                blue[8 - i] += Y * blue[9 - i]
                blue[9 - i] = 0
                break
    if state == 2:
        break


print(blue[0])
