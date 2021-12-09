import sys
input = sys.stdin.read().strip().split("\n")
n = len(input)
m = len(input[0])
def hi(i, j, input, lvl):
    if i < 0 or j < 0 or i >= n or j >= m:
        return True
    return int(input[i][j]) > int(lvl)
ans = 0
for i in range(n):
    for j in range(m):
        ofs = [(0,1), (1,0), (-1,0),(0,-1)]
        if False in (hi(i+x[0], j+x[1], input, input[i][j]) for x in ofs):
            continue
        ans += 1+int(input[i][j])
print(ans)
