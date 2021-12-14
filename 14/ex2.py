import sys
import collections
poly, input2 = sys.stdin.read().strip().split("\n\n")
input2 = input2.split("\n")
mp = {}
for x in input2:
    a, b = x.split(" -> ")
    mp[a] = b
pmp = collections.defaultdict(int)
cnt = collections.defaultdict(int)
for c in poly:
    cnt[c] += 1
for i in range(len(poly)-1):
    pmp[poly[i:i+2]] += 1
for _ in range(40):
    poly2 = []
    for x in dict(pmp).items():
        if x[0] in mp.keys():
            pmp[x[0][0]+mp[x[0]]] += x[1]
            pmp[mp[x[0]]+x[0][1]] += x[1]
            pmp[x[0]] -= x[1]
            cnt[mp[x[0]]] += x[1]
ans = sorted([(x[1], x[0]) for x in cnt.items()])
print(ans[-1][0]-ans[0][0])
