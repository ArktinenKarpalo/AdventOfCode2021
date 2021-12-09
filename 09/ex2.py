import sys
input = sys.stdin.read().strip().split("\n")
vis = set()
n = len(input)
m = len(input[0])
ans = []
def hi(i, j, input):
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    if (i, j) in vis or input[i][j] == '9':
        return 0
    vis.add((i,j))
    ofs = [(0,1), (1,0), (-1,0),(0,-1)]
    return sum(hi(i+x[0], j+x[1], input) for x in ofs)+1
for i in range(n):
    for j in range(m):
        ans.append(hi(i, j, input))
ans = sorted(ans)
print(ans[-1]*ans[-2]*ans[-3])
