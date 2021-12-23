import sys
import bisect
import re
input = sys.stdin.read().strip().split("\n")
sm = 0
cbd = []
for x in input:
    rs = re.match("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", x).groups()
    rs = [rs[0]]+[int(x) for x in rs[1:]]
    cbd.append(rs)
cbd2 = list(cbd)
for ao in range(3):
    cbd = list(map(lambda x: [x[0]]+x[5:7]+x[1:5], cbd))
    cbd2 = list(map(lambda x: [x[0]]+x[5:7]+x[1:5], cbd2))
    cts = []
    for cc in cbd:
        for ct in [cc[1]-1, cc[2]]:
            cts.append(ct)
    cts = sorted(set(cts))
    cn = []
    print(len(cbd2))
    for c2 in cbd2:
        cur = c2
        cbd3 = []
        for ct in cts[bisect.bisect_left(cts, c2[1]):bisect.bisect_right(cts, c2[1+1])+1]:
            if cur[1] <= ct and ct < cur[2]:
                c2 = list(cur)
                c2[2] = ct
                cur[1] = ct+1
                cbd3.append(c2)
        cbd3.append(cur)
        cn += cbd3
    cbd2 = cn
print(len(cbd2))

on = set()
for c in cbd2:
    if c[0] == "on":
        on.add(tuple(c[1:]))
    else:
        if tuple(c[1:]) in on:
            on.remove(tuple(c[1:]))

for c in on:
    sm += (c[1]-c[0]+1)*(c[3]-c[2]+1)*(c[5]-c[4]+1)


print(sm)
