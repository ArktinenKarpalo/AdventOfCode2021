
import sys
import collections
input = sys.stdin.read().strip().split("\n")

mp = collections.defaultdict(int)

for x in input:
    p = list(map(lambda x: list(map(int, x.strip().split(","))), x.split("->")))
    xa = 1 if p[0][0] < p[1][0] else -1
    ya = 1 if p[0][1] < p[1][1] else -1
    if p[1][0] == p[0][0]:
        for x in range(abs(p[1][1]-p[0][1])+1):
            mp[(p[0][0], p[0][1]+x*ya)] += 1
    elif p[1][1] == p[0][1]:
        for x in range(abs(p[1][0]-p[0][0])+1):
            mp[(p[0][0]+x*xa, p[0][1])] += 1
    else:
        pass
ans = 0
for x in mp.values():
    if x > 1:
        ans += 1
print(ans)
