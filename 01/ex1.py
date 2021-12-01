import sys
heights = list(map(int, sys.stdin.read().strip().split("\n")))
ans = 0
for i in range(1, len(heights)):
    if heights[i-1] < heights[i]:
        ans += 1
print(ans)
