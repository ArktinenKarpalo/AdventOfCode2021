import sys
import collections
input = sys.stdin.read().strip().split("\n")

con = collections.defaultdict(list)

for x in input:
    a, b = x.split("-")
    con[a].append(b)
    con[b].append(a)

vis = collections.defaultdict(int)
def s(cur, extra):
    if cur == "end":
        return 1
    if cur.islower() and vis[cur] > 0:
        if extra and cur != "start":
            extra = False
        else:
            return 0
    vis[cur] += 1
    ret = 0
    for u in con[cur]:
        ret += s(u, extra)
    vis[cur] -= 1
    return ret

print(s("start", True))
