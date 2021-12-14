import sys
import collections
poly, input2 = sys.stdin.read().strip().split("\n\n")
input2 = input2.split("\n")
mp = {}
for x in input2:
    a, b = x.split(" -> ")
    mp[a] = b
for _ in range(10):
    poly2 = []
    for i in range(len(poly)-1):
        poly2.append(poly[i])
        if poly[i:i+2] in mp.keys():
            poly2.append(mp[poly[i:i+2]])
    poly2.append(poly[-1])
    poly = "".join(poly2)
cnt = collections.defaultdict(int)
for c in poly:
    cnt[c] += 1
ans = sorted([(x[1], x[0]) for x in cnt.items()])
print(ans[-1][0]-ans[0][0])
