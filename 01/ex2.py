import sys
heights = list(map(int, sys.stdin.read().strip().split("\n")))
ans = 0
A = sum(heights[0:3])
B = sum(heights[1:4])
if A < B:
    ans += 1
for i in range(4, len(heights)):
    A -= heights[i-4]
    A += heights[i-1]
    B -= heights[i-3]
    B += heights[i]
    if A < B:
        ans += 1
print(ans)
