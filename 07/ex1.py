import sys
import collections
input = list(map(int, sys.stdin.read().split(",")))
ans = 1e9
right = len(input)
left = 0
sm = sum(input)
col = collections.defaultdict(int)
for x in input:
    col[x] += 1
for i in range(0, max(input)+1):
    ans = min(sm, ans)
    right -= col[i]
    sm -= right
    left += col[i]
    sm += left
print(ans)
