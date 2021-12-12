import sys
import collections
input = sys.stdin.read().strip().split("\n")

con = collections.defaultdict(list)

for x in input:
    a, b = x.split("-")
    con[a].append(b)
    con[b].append(a)

vis = collections.defaultdict(int)
def s(cur):
    if cur.islower() and vis[cur] > 0:
        return 0
    if cur == "end":
        return 1
    vis[cur] += 1
    ret = 0
    for u in con[cur]:
        ret += s(u)
    vis[cur] -= 1
    return ret

print(s("start"))
