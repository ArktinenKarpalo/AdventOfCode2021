import sys
input = sys.stdin.read().strip().split("\n")
input = [[int(y) for y in x] for x in input]
def oob(i, j):
    return i < 0 or j < 0 or j >= 10 or i >= 10
def fl(i, j):
    cnt = 1
    for x in range(-1, 1+1):
        for y in range(-1, 1+1):
            if (x == y and x == 0) or oob(i+x,j+y):
                continue
            input[i+x][j+y] += 1
            if input[i+x][j+y] == 10:
                cnt += fl(i+x, j+y)
    return cnt
for stp in range(100000):
    ans = 0
    for i in range(10):
        for j in range(10):
            input[i][j] += 1
            if input[i][j] == 10:
                ans += fl(i, j)
    for i in range(10):
        for j in range(10):
            if input[i][j] > 9:
                input[i][j] = 0
    if ans == 10*10:
        print(stp+1)
        exit(0)
