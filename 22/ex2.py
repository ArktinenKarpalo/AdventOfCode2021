import sys
import itertools
import re
input = sys.stdin.read().strip().split("\n")
sm = 0
cbd = []
for x in input:
    rs = re.match("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", x).groups()
    rs = [rs[0]]+[int(x) for x in rs[1:]]
    cbd.append(rs)

def cn(dim, cbdf, sz):
    if len(cbdf) == 0:
        return
    global sm
    if dim == 3:
        if cbdf[-1][0] == "on":
            sm += sz
        return
    lst = sorted(list(itertools.chain.from_iterable([x[1+dim*2], x[1+dim*2+1]] for x in cbdf)))
    lt = lst[0]-1
    for p in lst:
        if p+1 == lt:
            continue
        if p != lt:
            cbdf2 = list(filter(lambda x: x[1+dim*2] <= lt and lt <= x[1+dim*2+1], cbdf))
            cn(dim+1, cbdf2, sz*(p-lt))
        cbdf2 = list(filter(lambda x: x[1+dim*2] <= p and p <= x[1+dim*2+1], cbdf))
        cn(dim+1, cbdf2, sz*(1))
        lt = p+1


cn(0, cbd, 1)

print(sm)
